import Layout from '../Layout'
import {
  BsArrowDownLeft,
  BsArrowDownRight,
  BsArrowUpRight,
  BsCheckCircleFill,
  BsClockFill,
  BsXCircleFill,
} from 'react-icons/bs'
import { DashboardBigChart, DashboardSmallChart } from '../components/Charts'
import {
  appointmentsData,
  dashboardCards,
  memberData,
  reviewData,
  transactionData,
} from '../components/Datas'
import { Transactiontable } from '../components/Tables'
import { Link } from 'react-router-dom'
import { FaStar } from 'react-icons/fa'

function Dashboard() {
  return (
    <Layout>
      {/* boxes */}
      <div className="grid w-full grid-cols-1 gap-6 xl:grid-cols-4 lg:grid-cols-3 sm:grid-cols-2">
        {dashboardCards.map((card, index) => (
          <div
            key={card.id}
            className=" bg-white rounded-xl border-[1px] border-border p-5"
          >
            <div className="flex items-center gap-4">
              <div
                className={`w-10 h-10 flex-colo bg-opacity-10 rounded-md ${card.color[1]} ${card.color[0]}`}
              >
                <card.icon />
              </div>
              <h2 className="text-sm font-medium">{card.title}</h2>
            </div>
            <div className="grid items-center grid-cols-8 gap-4 px-8 py-5 mt-4 bg-dry rounded-xl">
              <div className="col-span-5">
                {/* statistc */}
                <DashboardSmallChart data={card.datas} colors={card.color[2]} />
              </div>
              <div className="flex flex-col col-span-3 gap-4">
                <h4 className="font-medium text-md">
                  {card.value}
                  {
                    // if the id === 4 then add the $ sign
                    card.id === 4 ? '$' : '+'
                  }
                </h4>
                <p className={`text-sm flex gap-2 ${card.color[1]}`}>
                  {card.percent > 50 && <BsArrowUpRight />}
                  {card.percent > 30 && card.percent < 50 && (
                    <BsArrowDownRight />
                  )}
                  {card.percent < 30 && <BsArrowDownLeft />}
                  {card.percent}%
                </p>
              </div>
            </div>
          </div>
        ))}
      </div>
      <div className="grid w-full grid-cols-1 gap-6 my-6 xl:grid-cols-8">
        <div className="w-full xl:col-span-6">
          {/* eye banner */}
          <div className=" bg-white rounded-xl border-[1px] border-border relative">
            <img
              src="/images/banner.avif"
              className="object-cover w-full rounded h-72"
              alt="banner"
            />
            <div className="absolute top-0 bottom-0 left-0 right-0 flex flex-col justify-center px-6 py-5 space-y-4 md:px-12 bg-subMain bg-opacity-10">
              <h1 className="text-xl font-semibold capitalize text-subMain">
                The future of eye care is here
              </h1>
              <p className="text-xs leading-6 text-textGray max-w-96">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor asin cididunt ut labore et dolore magna ali qua.
                Lorem ipsum dolor sit amet.
              </p>
              <div>
                {' '}
                <button className="px-6 py-3 text-xs text-white rounded bg-subMain flex-colo transitions">
                  Read More
                </button>
              </div>
            </div>
          </div>
          <div className="mt-6 bg-white rounded-xl border-[1px] border-border p-5">
            <div className="gap-2 flex-btn">
              <h2 className="text-sm font-medium">Earning Reports</h2>
              <p className="flex items-center gap-4 text-sm">
                5.44%{' '}
                <span className="px-2 py-1 text-xs text-white bg-subMain rounded-xl">
                  +2.4%
                </span>
              </p>
            </div>
            {/* Earning Reports */}
            <div className="mt-4">
              <DashboardBigChart />
            </div>
          </div>
          {/* transaction */}
          <div className="mt-6 bg-white rounded-xl border-[1px] border-border p-5">
            <div className="gap-2 flex-btn">
              <h2 className="text-sm font-medium">Recent Transaction</h2>
              <p className="flex items-center gap-4 text-sm">
                Today{' '}
                <span className="px-2 py-1 text-xs text-white bg-subMain rounded-xl">
                  27000$
                </span>
              </p>
            </div>
            {/* table */}
            <div className="mt-4 overflow-x-scroll">
              <Transactiontable
                data={transactionData.slice(0, 5)}
                action={false}
              />
            </div>
          </div>
        </div>
        {/* side 2 */}
        <div
          data-aos="fade-left"
          data-aos-duration="1000"
          data-aos-delay="10"
          data-aos-offset="200"
          className="grid gap-6 xl:col-span-2 xl:block sm:grid-cols-2"
        >
          {/* review */}
          <div className="bg-white rounded-xl border-[1px] border-border p-5">
            <h2 className="text-sm font-medium">Recent Reviews</h2>
            {reviewData.slice(1, 3).map((rev, index) => (
              <div
                key={index}
                className="gap-4 pb-4 mt-6 border-b flex-btn border-border"
              >
                <div className="flex items-center gap-4">
                  <img
                    src={rev?.user?.image}
                    alt={rev?.user?.title}
                    className="object-cover w-10 h-10 rounded-md"
                  />
                  <div className="flex flex-col gap-1">
                    <h3 className="text-xs font-medium">{rev?.user?.title}</h3>
                    <p className="text-xs leading-5 text-gray-400 truncate text-wrap max-w-44">
                      {rev?.comment.slice(0, 45)}...
                    </p>
                  </div>
                </div>
                <div className="gap-1 flex-rows">
                  <p className="text-xs text-textGray">{rev?.star}</p>
                  <p className="text-xs text-orange-500">
                    <FaStar />
                  </p>
                </div>
              </div>
            ))}
          </div>
          {/* recent patients */}
          <div className="bg-white rounded-xl border-[1px] border-border p-5 xl:mt-6">
            <h2 className="text-sm font-medium">Recent Patients</h2>
            {memberData.slice(3, 8).map((member, index) => (
              <Link
                to={`/patients/preview/${member.id}`}
                key={index}
                className="gap-4 pb-4 mt-6 border-b flex-btn border-border"
              >
                <div className="flex items-center gap-4">
                  <img
                    src={member.image}
                    alt="member"
                    className="object-cover w-10 h-10 rounded-md"
                  />
                  <div className="flex flex-col gap-1">
                    <h3 className="text-xs font-medium">{member.title}</h3>
                    <p className="text-xs text-gray-400">{member.phone}</p>
                  </div>
                </div>
                <p className="text-xs text-textGray">2:00 PM</p>
              </Link>
            ))}
          </div>
          {/* today apointments */}
          <div className="bg-white rounded-xl border-[1px] border-border p-5 xl:mt-6">
            <h2 className="mb-4 text-sm font-medium">Today Appointments</h2>
            {appointmentsData.map((appointment, index) => (
              <div
                key={appointment.id}
                className="grid items-center grid-cols-12 gap-2"
              >
                <p className="text-textGray text-[12px] col-span-3 font-light">
                  {appointment.time}
                </p>
                <div className="relative col-span-2 flex-colo">
                  <hr className="w-[2px] h-20 bg-border" />
                  <div
                    className={`w-7 h-7 flex-colo text-sm bg-opacity-10
                   ${
                     appointment.status === 'Pending' &&
                     'bg-orange-500 text-orange-500'
                   }
                  ${
                    appointment.status === 'Cancel' && 'bg-red-500 text-red-500'
                  }
                  ${
                    appointment.status === 'Approved' &&
                    'bg-green-500 text-green-500'
                  }
                   rounded-full absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2`}
                  >
                    {appointment.status === 'Pending' && <BsClockFill />}
                    {appointment.status === 'Cancel' && <BsXCircleFill />}
                    {appointment.status === 'Approved' && <BsCheckCircleFill />}
                  </div>
                </div>
                <Link
                  to="/appointments"
                  className="flex flex-col col-span-6 gap-1"
                >
                  <h2 className="text-xs font-medium">
                    {appointment.user?.title}
                  </h2>
                  <p className="text-[12px] font-light text-textGray">
                    {appointment.from} - {appointment.to}
                  </p>
                </Link>
              </div>
            ))}
          </div>
        </div>
      </div>
    </Layout>
  )
}

export default Dashboard
