import { MorphLabsApiClient } from './gen/Client';

declare module 'morphcloud' {
  interface MorphCloudClient {
    browsers: MorphLabsApiClient;
  }
}