import * as SecureStore from 'expo-secure-store';

const options: SecureStore.SecureStoreOptions = { keychainAccessible: SecureStore.WHEN_UNLOCKED_THIS_DEVICE_ONLY };
export const secureSessionStorage = {
  getItem: (key: string) => SecureStore.getItemAsync(`polskiflow.${key}`, options),
  setItem: (key: string, value: string) => SecureStore.setItemAsync(`polskiflow.${key}`, value, options),
  removeItem: (key: string) => SecureStore.deleteItemAsync(`polskiflow.${key}`, options),
};
