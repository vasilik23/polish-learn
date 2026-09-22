export type Colors = ReturnType<typeof palette>;
export function palette(dark: boolean) {
  return dark
    ? { background: '#101712', surface: '#17221a', text: '#f3f7f4', muted: '#abc0af', primary: '#73db8c', border: '#304638', danger: '#ffb4ab' }
    : { background: '#f5f8f3', surface: '#ffffff', text: '#172119', muted: '#58695b', primary: '#176b35', border: '#d8e3d8', danger: '#a3261c' };
}
