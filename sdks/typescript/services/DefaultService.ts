/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { MetadataUpdateRequest } from '../models/MetadataUpdateRequest';
import type { RecordingList } from '../models/RecordingList';
import type { Session } from '../models/Session';
import type { SessionList } from '../models/SessionList';
import type { CancelablePromise } from '../core/CancelablePromise';
import type { BaseHttpRequest } from '../core/BaseHttpRequest';
export class DefaultService {
    constructor(public readonly httpRequest: BaseHttpRequest) {}
    /**
     * List Sessions
     * @returns SessionList Successful Response
     * @throws ApiError
     */
    public listSessions(): CancelablePromise<SessionList> {
        return this.httpRequest.request({
            method: 'GET',
            url: '/session',
        });
    }
    /**
     * Create Session
     * Create a new browser session.
     *
     * If resource limits are reached, return an existing session for the user
     * instead of failing with 500.
     * @param name
     * @param viewportWidth
     * @param viewportHeight
     * @returns Session Successful Response
     * @throws ApiError
     */
    public createSession(
        name?: (string | null),
        viewportWidth?: (number | null),
        viewportHeight?: (number | null),
    ): CancelablePromise<Session> {
        return this.httpRequest.request({
            method: 'POST',
            url: '/session',
            query: {
                'name': name,
                'viewport_width': viewportWidth,
                'viewport_height': viewportHeight,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Session Connect Url
     * @param id
     * @returns any Successful Response
     * @throws ApiError
     */
    public getSessionConnectUrl(
        id: string,
    ): CancelablePromise<any> {
        return this.httpRequest.request({
            method: 'GET',
            url: '/session/{id}/connect',
            path: {
                'id': id,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Session
     * @param id
     * @returns Session Successful Response
     * @throws ApiError
     */
    public getSession(
        id: string,
    ): CancelablePromise<Session> {
        return this.httpRequest.request({
            method: 'GET',
            url: '/session/{id}',
            path: {
                'id': id,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Stop Session
     * @param id
     * @returns Session Successful Response
     * @throws ApiError
     */
    public stopSession(
        id: string,
    ): CancelablePromise<Session> {
        return this.httpRequest.request({
            method: 'DELETE',
            url: '/session/{id}',
            path: {
                'id': id,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Session By Name
     * @param name
     * @returns Session Successful Response
     * @throws ApiError
     */
    public getSessionByName(
        name: string,
    ): CancelablePromise<Session> {
        return this.httpRequest.request({
            method: 'GET',
            url: '/session/{name}/by-name',
            path: {
                'name': name,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Pause Session
     * Pause a running browser session (VM pause).
     * @param id
     * @returns Session Successful Response
     * @throws ApiError
     */
    public pauseSession(
        id: string,
    ): CancelablePromise<Session> {
        return this.httpRequest.request({
            method: 'POST',
            url: '/session/{id}/pause',
            path: {
                'id': id,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Resume Session
     * Resume a previously paused browser session.
     * @param id
     * @returns Session Successful Response
     * @throws ApiError
     */
    public resumeSession(
        id: string,
    ): CancelablePromise<Session> {
        return this.httpRequest.request({
            method: 'POST',
            url: '/session/{id}/resume',
            path: {
                'id': id,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Branch Session
     * Branch an existing session into N replicas.
     *
     * Each branched session receives a new `browsers:id` while inheriting the
     * parent's recording state via a shared `browsers:recording_id`.
     * @param id
     * @param replicas
     * @returns SessionList Successful Response
     * @throws ApiError
     */
    public branchSession(
        id: string,
        replicas: number = 1,
    ): CancelablePromise<SessionList> {
        return this.httpRequest.request({
            method: 'POST',
            url: '/session/{id}/branch',
            path: {
                'id': id,
            },
            query: {
                'replicas': replicas,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Update Session Metadata
     * Update per-session metadata stored on the instance.
     * - `metadata` is stored serialized under `browsers:meta` (JSON string).
     * @param id
     * @param requestBody
     * @returns Session Successful Response
     * @throws ApiError
     */
    public updateSessionMetadata(
        id: string,
        requestBody: MetadataUpdateRequest,
    ): CancelablePromise<Session> {
        return this.httpRequest.request({
            method: 'POST',
            url: '/session/{id}/metadata',
            path: {
                'id': id,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Share Session
     * @param id
     * @param ttlSeconds
     * @returns any Successful Response
     * @throws ApiError
     */
    public shareSession(
        id: string,
        ttlSeconds: number = 900,
    ): CancelablePromise<any> {
        return this.httpRequest.request({
            method: 'POST',
            url: '/session/{id}/share',
            path: {
                'id': id,
            },
            query: {
                'ttl_seconds': ttlSeconds,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * List Recordings
     * @param id
     * @returns RecordingList Successful Response
     * @throws ApiError
     */
    public listRecordings(
        id: string,
    ): CancelablePromise<RecordingList> {
        return this.httpRequest.request({
            method: 'GET',
            url: '/session/{id}/recordings',
            path: {
                'id': id,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Start Recording
     * @param id
     * @param recordingId
     * @param name
     * @param description
     * @returns any Successful Response
     * @throws ApiError
     */
    public startRecording(
        id: string,
        recordingId?: (string | null),
        name?: (string | null),
        description?: (string | null),
    ): CancelablePromise<any> {
        return this.httpRequest.request({
            method: 'POST',
            url: '/session/{id}/recordings/start',
            path: {
                'id': id,
            },
            query: {
                'recording_id': recordingId,
                'name': name,
                'description': description,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Stop Recording
     * @param id
     * @param rid
     * @returns any Successful Response
     * @throws ApiError
     */
    public stopRecording(
        id: string,
        rid: string,
    ): CancelablePromise<any> {
        return this.httpRequest.request({
            method: 'POST',
            url: '/session/{id}/recordings/{rid}/stop',
            path: {
                'id': id,
                'rid': rid,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Recording Events Raw
     * @param id
     * @param rid
     * @returns any Successful Response
     * @throws ApiError
     */
    public getRecordingEventsRaw(
        id: string,
        rid: string,
    ): CancelablePromise<any> {
        return this.httpRequest.request({
            method: 'GET',
            url: '/session/{id}/recordings/{rid}/events.ndjson',
            path: {
                'id': id,
                'rid': rid,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
}
