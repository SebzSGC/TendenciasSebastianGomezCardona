import { FaCheckCircle } from 'react-icons/fa'

export default function SuccessStep() {
  return (
    <div className="p-6 text-center">
      <FaCheckCircle className="w-16 h-16 mx-auto mb-4 text-green-500 animate__animated animate__bounceIn" />
      <h2 className="mb-2 text-2xl font-semibold">
        ¡Datos guardados con éxito!
      </h2>
      <p className="text-gray-600">
        Gracias por proporcionar toda la información necesaria.
      </p>
    </div>
  )
}
