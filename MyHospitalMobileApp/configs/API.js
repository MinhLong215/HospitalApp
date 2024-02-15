import axios from "axios";

// const HOST = 'http://127.0.0.1:8000/'

export const endpoints = {
    'login': '/o/token/',
    'current-user': '/users/current_user/'
}

export const authApi = (accessToken) => axios.create({
    baseURL: "http://127.0.0.1:8000", 
    headers: {
        "Authorization": `bearer ${accessToken}`
    }
})

export default axios.create({
    baseURL: "http://127.0.0.1:8000"
})