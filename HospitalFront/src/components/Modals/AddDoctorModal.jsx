import { useState } from 'react'
import { useField } from '../../hooks/useField'
import Modal from './Modal'
import { Button, Input, Select } from '../Form'
import { BiChevronDown } from 'react-icons/bi'
import { sortsDatas } from '../Datas'
import { HiOutlineCheckCircle } from 'react-icons/hi'
import { toast } from 'react-hot-toast'
import Access from '../Access'
import Uploader from '../Uploader'

function AddDoctorModal({ closeModal, isOpen, doctor, datas }) {
  const [instruction, setInstruction] = useState(sortsDatas.title[0])
  const [access, setAccess] = useState({})
  const fullName = useField()
  const email = useField()
  const phoneNumber = useField()
  const password = useField()

  const onSubmit = () => {
    const doctor = {
      fullName: fullName.value,
      email: email.value,
      phoneNumber: phoneNumber.value,
      password: password.value,
      title: instruction.name,
      access: { access },
    }
    console.log(doctor)
    toast.error('This feature is not available yet')
  }

  return (
    <Modal
      closeModal={closeModal}
      isOpen={isOpen}
      title={doctor ? 'Add Doctor' : datas?.id ? 'Edit Stuff' : 'Add Stuff'}
      width={'max-w-3xl'}
    >
      <div className="flex flex-col col-span-6 gap-3 mb-6">
        <p className="text-sm">Profile Image</p>
        <Uploader />
      </div>

      <div className="gap-6 flex-colo">
        <div className="grid w-full gap-4 sm:grid-cols-2">
          <Input
            label="Full Name"
            color={true}
            type="text"
            name="fullName"
            register={fullName}
          />

          <div className="flex flex-col w-full gap-3">
            <p className="text-sm text-black">Title</p>
            <Select
              selectedPerson={instruction}
              setSelectedPerson={setInstruction}
              datas={sortsDatas.title}
            >
              <div className="w-full p-4 text-sm font-light border rounded-lg flex-btn text-textGray border-border focus:border focus:border-subMain">
                {setInstruction.name} <BiChevronDown className="text-xl" />
              </div>
            </Select>
          </div>
        </div>

        <div className="grid w-full gap-4 sm:grid-cols-2">
          <Input
            label="Email"
            color={true}
            type="text"
            name="email"
            register={email}
          />
          <Input
            label="Phone Number"
            color={true}
            type="number"
            name="phoneNumber"
            register={phoneNumber}
          />
        </div>

        {/* password */}
        <Input
          label="Password"
          color={true}
          type="text"
          name="password"
          register={password}
        />

        {/* table access */}
        <div className="w-full">
          <Access setAccess={setAccess} />
        </div>

        {/* buttons */}
        <div className="grid w-full gap-4 sm:grid-cols-2">
          <button
            onClick={closeModal}
            className="p-4 text-sm font-light text-red-600 bg-red-600 rounded-lg bg-opacity-5"
          >
            Cancel
          </button>
          <Button label="Save" Icon={HiOutlineCheckCircle} onClick={onSubmit} />
        </div>
      </div>
    </Modal>
  )
}

export default AddDoctorModal
