import React from 'react';
import { FaLinkedin, FaGithub, FaEnvelope } from 'react-icons/fa';
import { motion } from 'framer-motion';

const teamMembers = [
  {
    name: "Priyanshu Singhal",
    bio: "Co-creator of WatCourse. Passionate about building impactful student tools and simplifying course planning.",
    image: "../assets/background1.png",
    linkedin: "https://linkedin.com/in/priyanshusinghal12",
    github: "https://github.com/priyanshusinghal12",
    email: "mailto:priyanshu@example.com",
    imageLeft: true,
  },
  {
    name: "Ridhika Madan",
    bio: "Co-creator of WatCourse. Focused on innovation, strategy, and helping students design their academic journey with clarity.",
    image: "../assets/background1.png",
    linkedin: "https://linkedin.com/in/yourprofile",
    github: "https://github.com/yourgithub",
    email: "mailto:ridhika@example.com",
    imageLeft: false,
  },
];

const AboutUs = () => {
  return (
    <div className="bg-gray-950 text-white py-16 px-6">
      <h1 className="text-5xl font-bold text-center mb-20 tracking-wide">About Us</h1>
      <div className="space-y-24 max-w-6xl mx-auto">
        {teamMembers.map((member, index) => (
          <motion.div
            key={index}
            initial={{ opacity: 0, y: 50 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, ease: "easeOut" }}
            viewport={{ once: true }}
            className={`flex flex-col md:flex-row ${
              !member.imageLeft ? 'md:flex-row-reverse' : ''
            } items-center gap-10 md:gap-20`}
          >
            <motion.img
              src={member.image}
              alt={member.name}
              whileHover={{ scale: 1.05 }}
              transition={{ type: "spring", stiffness: 200 }}
              className="w-48 h-48 md:w-60 md:h-60 rounded-3xl object-cover shadow-xl border-4 border-gray-800"
            />
            <div className="text-center md:text-left max-w-xl">
              <h2 className="text-3xl font-semibold mb-4">{member.name}</h2>
              <p className="text-gray-300 text-lg mb-6 leading-relaxed">
                {member.bio}
              </p>
              <div className="flex justify-center md:justify-start gap-6 text-2xl">
                <motion.a
                  href={member.linkedin}
                  target="_blank"
                  rel="noopener noreferrer"
                  whileHover={{ scale: 1.2 }}
                >
                  <FaLinkedin className="hover:text-blue-400 transition duration-200" />
                </motion.a>
                <motion.a
                  href={member.github}
                  target="_blank"
                  rel="noopener noreferrer"
                  whileHover={{ scale: 1.2 }}
                >
                  <FaGithub className="hover:text-gray-400 transition duration-200" />
                </motion.a>
                <motion.a
                  href={member.email}
                  whileHover={{ scale: 1.2 }}
                >
                  <FaEnvelope className="hover:text-red-400 transition duration-200" />
                </motion.a>
              </div>
            </div>
          </motion.div>
        ))}
      </div>
    </div>
  );
};

export default AboutUs;
