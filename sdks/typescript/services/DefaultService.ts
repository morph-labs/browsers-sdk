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
     * @returns SessionList OK
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
     * @param name
     * @returns Session OK
     * @throws ApiError
     */
    public createSession(
        name?: (string | null),
    ): CancelablePromise<Session> {
        return this.httpRequest.request({
            method: 'POST',
            url: '/session',
            query: {
                'name': name,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Session
     * @param id
     * @returns Session OK
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
     * @returns Session OK
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
     * @returns Session OK
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
}
