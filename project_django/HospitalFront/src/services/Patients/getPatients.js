import axios from 'axios'

async function getPatients() {
  try {
    const response = await axios.get('http://127.0.0.1:8000/hospital/patients')
    return response.data
  } catch (error) {
    console.error(error)
    return []
  }
}

export default getPatients
