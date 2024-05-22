import { HiArrowNarrowLeft, HiArrowNarrowRight } from 'react-icons/hi'
import { Button, Input } from '../Form'
import { useForm } from 'react-hook-form'
import { yupResolver } from '@hookform/resolvers/yup'
import { ContactValidation } from '../Validation'
import toast from 'react-hot-toast'
import { useState } from 'react'

export function EmergencyContact({ nextStep, backStep, button = true }) {
  const [isLoading, setIsLoading] = useState(false)
  const onSubmit = data => {
    setIsLoading(true)
    const saveContactPromise = new Promise((resolve, reject) => {
      setTimeout(() => {
        const contact = {
          ...data,
          idPatient: JSON.parse(sessionStorage.getItem('patient')).idDocument,
        }
        if (contact) {
          sessionStorage.setItem('contact', JSON.stringify(contact))
          resolve(contact.fullName)
          nextStep()
          setIsLoading(false)
        } else {
          reject('Error al guardar el contacto de emergencia')
        }
      }, 3000)
    })

    toast.promise(saveContactPromise, {
      loading: 'Guardando contacto...',
      success: fullName => `contacto ${fullName} guardado con éxito`,
      error: err => err,
    })
  }
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm({
    resolver: yupResolver(ContactValidation),
  })
  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <div className="gap-4 flex-colo">
        <div className="flex flex-col w-full gap-3">
          <p className="my-5 text-base text-center text-black">
            Contacto de emergencia
          </p>
          <div className="grid w-full gap-2 sm:grid-cols-3">
            <Input
              label="Nombre Completo"
              color={true}
              type="text"
              register={register('fullName')}
              error={errors.fullName}
            />
            <Input
              label="Relacion"
              color={true}
              type="text"
              register={register('relationship')}
              error={errors.relationship}
            />
            <Input
              label="Telefono"
              color={true}
              type="number"
              register={register('phoneNumber')}
              error={errors.phoneNumber}
            />
          </div>
        </div>
        {/* submit */}
        {button && (
          <div className="grid w-full grid-cols-1 gap-4 my-5 sm:grid-cols-2">
            <Button
              Icon={HiArrowNarrowLeft}
              IconLeft={true}
              label="Regresar"
              loading={isLoading}
              onClick={() => {
                backStep()
              }}
            />
            <Button
              label={'Continuar'}
              Icon={HiArrowNarrowRight}
              loading={isLoading}
              onSubmit={onSubmit}
            />
          </div>
        )}
      </div>
    </form>
  )
}
