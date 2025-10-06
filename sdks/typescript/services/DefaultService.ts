/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
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
}
