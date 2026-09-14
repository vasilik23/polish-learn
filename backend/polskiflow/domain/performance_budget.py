from dataclasses import asdict, dataclass
from pathlib import Path
import json
import statistics


class LighthouseReportError(ValueError):
    pass


@dataclass(frozen=True)
class LighthouseMedian:
    score: float
    accessibility_score: float
    lcp_ms: float
    cls: float
    tbt_ms: float
    ttfb_ms: float

    def as_dict(self):
        return asdict(self)


def _number(value, label):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise LighthouseReportError(f"{label} must be numeric")
    return float(value)


def load_lighthouse_report(path):
    try:
        payload = json.loads(Path(path).read_text(encoding="utf-8"))
        audits = payload["audits"]
        score = payload["categories"]["performance"]["score"]
        accessibility_score = payload["categories"]["accessibility"]["score"]
        values = (
            _number(score, "performance score") * 100,
            _number(accessibility_score, "accessibility score") * 100,
            _number(audits["largest-contentful-paint"]["numericValue"], "LCP"),
            _number(audits["cumulative-layout-shift"]["numericValue"], "CLS"),
            _number(audits["total-blocking-time"]["numericValue"], "TBT"),
            _number(audits["server-response-time"]["numericValue"], "TTFB"),
        )
    except (OSError, json.JSONDecodeError, KeyError, TypeError) as exc:
        raise LighthouseReportError(f"Invalid Lighthouse report: {path}") from exc
    return values


def evaluate_lighthouse_reports(paths):
    if len(paths) < 3:
        raise LighthouseReportError("At least three sequential reports are required")
    rows = [load_lighthouse_report(path) for path in paths]
    median = LighthouseMedian(*(statistics.median(column) for column in zip(*rows)))
    failures = []
    if median.score < 90:
        failures.append("score < 90")
    if median.accessibility_score < 95:
        failures.append("accessibility score < 95")
    if median.lcp_ms > 2500:
        failures.append("LCP > 2500 ms")
    if median.cls > 0.1:
        failures.append("CLS > 0.1")
    if median.tbt_ms > 200:
        failures.append("TBT > 200 ms")
    return median, failures
