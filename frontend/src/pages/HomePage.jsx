import React from "react";
import ImageAndLink from "../components/ImageAndLink";
import resume from "../assets/images/resume.jpg";

const HomePage = () => {
  return (
    <>
      <div className="flex justify-center items-center  pt-2">
        <div className=" font-bold mt-28 rounded-md mx-auto my-auto text-2xl">
          Welcome to ResumeWonder
        </div>
      </div>
      <div className="flex justify-center items-center pb-4 font-medium">
        Craft Your Perfect Resume with Ease & Elevate Your Job Application
        Effortlessly
      </div>
      <div className="grid grid-cols-5 gap-2 justify-items-center align-items-center pt-4">
        <div></div>
        <ImageAndLink
          imageSrc={resume}
          imageAlt="photo of man"
          linkLabel="Create New Resume"
          linkTarget="resume-editor/"
        />
        <ImageAndLink
          imageSrc={resume}
          imageAlt="photo of man"
          linkLabel="View Existing Resumes"
          linkTarget="existing-resumes/"
        />
        <ImageAndLink
          imageSrc={resume}
          imageAlt="photo of man"
          linkLabel="Export Resume"
          linkTarget="export-resume/"
        />
        <div></div>
      </div>
    </>
  );
};

export default HomePage;
