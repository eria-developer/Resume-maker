import React from "react";
import { Link } from "react-router-dom";

const ImageAndLink = ({ linkLabel, linkTarget, imageSrc, imageAlt }) => {
  return (
    <>
      <div>
        <img src={imageSrc} alt={imageAlt} className="rounded" />
        <div className="flex justify-center mt-4 bg-purple-500 rounded text-white font-semibold py-2">
          <Link to={linkTarget}>{linkLabel}</Link>
        </div>
      </div>
    </>
  );
};

export default ImageAndLink;
