import axios from 'axios';
const url = 'http://localhost:5000/api/products/';

class ProductService {
  static async getAll() {
    const res = await axios.get(url);

    try {
      const data = res.data;
      return data.map((product) => ({
        ...product,
        createdAt: new Date(product.createdAt),
      }));
    } catch (error) {
      return error;
    }
  }

  static show(id) {
    return axios.get(`${url}${id}`);
  }

  static create(product) {
    return axios.post(url, {
      product,
    });
  }

  static update(product) {
    return axios.put(`${url}${product.id}`, product);
  }

  static delete(id) {
    return axios.delete(`${url}${id}`);
  }
}
