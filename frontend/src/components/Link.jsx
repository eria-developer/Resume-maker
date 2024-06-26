import React from "react";
import { Link } from "react-router-dom";

const LinkComp = ({ linkLabel, linkTarget }) => {
  return (
    <>
      <div>
        <div className="flex justify-center px-4 mt-4 bg-purple-500 rounded text-white font-semibold py-2">
          <Link to={linkTarget}>{linkLabel}</Link>
        </div>
      </div>
    </>
  );
};

export default LinkComp;
