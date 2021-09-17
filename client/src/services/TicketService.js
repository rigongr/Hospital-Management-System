import axios from 'axios';
const url = 'http://localhost:5000/api/tickets/';

class TicketsService {
  static async getAll() {
    const res = await axios.get(url);

    try {
      const data = res.data;
      return data.map((ticket) => ({
        ...ticket,
        createdAt: new Date(ticket.createdAt),
      }));
    } catch (error) {
      return error;
    }
  }

  static show(id) {
    return axios.get(`${url}${id}`);
  }

  static create(ticket) {
    return axios.post(url, {
      ticket,
    });
  }

  static update(ticket) {
    return axios.put(`${url}${ticket.id}`, ticket);
  }

  static delete(id) {
    return axios.delete(`${url}${id}`);
  }
}
