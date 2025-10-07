/**
 * Browsers Plugin for MorphCloud SDK
 */

import { MorphLabsApiClient } from './gen/Client';
import * as MorphLabsApi from './gen/index';

// Import the type augmentation
import './types.d.ts';

export interface BrowsersClientOptions {
  browsersBaseUrl?: string;
}

/**
 * Create a service client from a MorphCloud client
 */
export function createServiceClient(
  morphClient: any,
  options: BrowsersClientOptions = {}
): MorphLabsApiClient {
  const baseUrl = options.browsersBaseUrl || 
    process.env.BROWSERS_BASE_URL || 
    'https://browsers.svc.cloud.morph.so';
  
  return new MorphLabsApiClient({
    environment: baseUrl,
    token: morphClient.apiKey,
  });
}

/**
 * Register the Browsers plugin with the main MorphCloud client
 */
export default function registerSDKPlugin(morphClient: any): void {
  // Add browsers property to the client
  Object.defineProperty(morphClient, 'browsers', {
    get() {
      return createServiceClient(morphClient);
    },
    enumerable: true,
    configurable: true
  });
}

// Alternative export for different import styles
export function morphcloudPlugin(morphClient: any): void {
  registerSDKPlugin(morphClient);
}

// Re-export the generated types and classes for direct usage
export { MorphLabsApiClient as BrowsersClient };
export { MorphLabsApi };