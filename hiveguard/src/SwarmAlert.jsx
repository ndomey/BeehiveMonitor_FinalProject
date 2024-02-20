import emailjs from "@emailjs/browser"


const showTime = new Date()
const currentTime = showTime.getHours()+':'+showTime.getMinutes()


const sendSwarmDetection = () => {

    emailjs.init(import.meta.env.VITE_EMAIL_USER_ID)
    emailjs
        .send(
            import.meta.env.VITE_EMAIL_SERVICE_ID,
            import.meta.env.VITE_EMAIL_TEMPLATE_ID,

            {
                to_email: 'domey.f@gmail.com',
                hive_number: '5',
                swarm_date:  currentTime,
            }
        )
}

export { sendSwarmDetection }