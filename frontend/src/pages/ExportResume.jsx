import React from "react";
import LinkComp from "../components/Link";

const HomePage = () => {
  return (
    <>
      <div className="flex justify-center  pt-2">
        <div className=" font-bold mt-16 rounded-md mx-auto my-auto text-2xl">
          Export Your Resume
        </div>
      </div>
      <div className="grid grid-cols-5 gap-2 justify-items-center pt-2">
        <div></div>
        <LinkComp linkLabel="Download as PDF" linkTarget="resume-editor/" />
        <LinkComp linkLabel="Download as Word" linkTarget="existing-resumes/" />
        <LinkComp linkLabel="Download as Text" linkTarget="export-resume/" />
        <div></div>
      </div>
    </>
  );
};

export default HomePage;
