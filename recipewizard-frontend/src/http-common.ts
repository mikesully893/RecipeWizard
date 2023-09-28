// import axios from "axios";

// export default axios.create({
//     baseURL: "http://localhost:5000",
//     headers: {
//         "Content-type": "application/json"
//     }
// });


const defaultHeaders = {
    "Content-Type": "application/json"
};
  
export function get(url: string, headers: HeadersInit = {}): Promise<Response> {
    return fetch(url, { headers: { ...defaultHeaders, ...headers },
                        method: "GET", });
}

export function remove(url: string, headers: HeadersInit = {}): Promise<Response> {
    return fetch(url, {
        headers: { ...defaultHeaders, ...headers },
        method: "DELETE",
    });
}

export function post(url: string, body: object, headers: HeadersInit = {}): Promise<Response> {
    return fetch(url, {
        headers: { ...defaultHeaders, ...headers },
        method: "POST",
        body: JSON.stringify(body),
    });
}

export function put(url: string, body: object, headers: HeadersInit = {}): Promise<Response> {
    return fetch(url, {
        headers: { ...defaultHeaders, ...headers },
        method: "PUT",
        body: JSON.stringify(body),
    });
}

export function patch(url: string, body: object, headers: HeadersInit = {}): Promise<Response> {
    return fetch(url, {
        headers: { ...defaultHeaders, ...headers },
        method: "PATCH",
        body: JSON.stringify(body),
    });
}