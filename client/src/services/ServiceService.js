import axios from 'axios';
const url = 'http://localhost:5000/api/services/';

class ServiceService {
  static async getAll() {
    const res = await axios.get(url);

    try {
      const data = res.data;
      return data.map((service) => ({
        ...service,
        createdAt: new Date(service.createdAt),
      }));
    } catch (error) {
      return error;
    }
  }

  static show(id) {
    return axios.get(`${url}${id}`);
  }

  static create(service) {
    return axios.post(url, {
      service,
    });
  }

  static update(service) {
    return axios.put(`${url}${service.id}`, service);
  }

  static delete(id) {
    return axios.delete(`${url}${id}`);
  }
}
