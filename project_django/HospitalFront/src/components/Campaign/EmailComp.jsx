import { Button, Input, Select, Textarea } from '../Form'
import { BiChevronDown } from 'react-icons/bi'
import Uploder from '../Uploader'
import { toast } from 'react-hot-toast'
import { sortsDatas } from '../Datas'
import { useState, useEffect } from 'react'

const sendToData = sortsDatas?.method.map(data => {
  return {
    id: data.id,
    name: data.name,
    value: data.name,
  }
})

function EmailComp({ data }) {
  const [sendTo, setSendTo] = useState(sendToData[0])
  const [image, setImage] = useState(null)

  // useEffect
  useEffect(() => {
    if (data?.id) {
      setSendTo(data.sendTo)
      setImage(data.image)
    }
  }, [data])

  return (
    <div className="flex flex-col w-full gap-4 mt-6">
      {/* title */}
      <Input
        label="Campaign Title"
        color={true}
        placeholder={data?.id && data?.title}
      />
      {/* send to */}
      <div className="grid gap-4 sm:grid-cols-2">
        <div className="flex flex-col w-full gap-3">
          <p className="text-sm">Send To</p>
          <Select
            selectedPerson={sendTo}
            setSelectedPerson={setSendTo}
            datas={sendToData}
          >
            <div className="flex items-center justify-between w-full px-4 text-xs bg-white border rounded-md h-14 text-main border-border">
              <p>{sendTo?.name}</p>
              <BiChevronDown className="text-xl" />
            </div>
          </Select>
        </div>
        {/* subject */}
        <Input
          label="Email subject"
          color={true}
          placeholder={data?.id && data?.action?.subject}
        />
      </div>
      {/* headers */}
      <div className="grid gap-4 sm:grid-cols-2">
        <Input
          label="Header"
          color={true}
          placeholder={data?.id && data?.action?.header}
        />
        <Input
          label="Sub-header"
          color={true}
          placeholder={data?.id && data?.action?.subHeader}
        />
      </div>
      {/* message */}
      <Textarea
        label="Message"
        placeholder={
          data?.id ? data?.action?.message : 'Dear Delight patient ....'
        }
        color={true}
        rows={5}
      />

      {/* uploader */}
      <div className="flex flex-col col-span-6 gap-3">
        <p className="text-sm">Image (option)</p>
        <Uploder />
      </div>
      {/* button */}
      {!data?.id && (
        <Button
          label={'Send Campaign'}
          onClick={() => {
            toast.error('This feature is not available yet')
          }}
        />
      )}
    </div>
  )
}

export default EmailComp
