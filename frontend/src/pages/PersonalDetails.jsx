import React from "react";

const PersonalDetails = () => {
  return (
    <div>
      <h2 className="text-2xl font-semibold mb-4">Personal Details</h2>
      {/* Add your form fields here */}
      <form>
        <div className="mb-4">
          <label className="block text-gray-700">Firstname</label>
          <input
            type="text"
            name="firstname"
            className="w-full px-3 py-2 border rounded"
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700">Othernames</label>
          <input
            type="text"
            name="othernames"
            className="w-full px-3 py-2 border rounded"
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700">Email</label>
          <input
            type="email"
            name="email"
            className="w-full px-3 py-2 border rounded"
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700">Phonenumber</label>
          <input
            type="text"
            name="phonenumber"
            className="w-full px-3 py-2 border rounded"
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700">Address</label>
          <textarea
            type="text"
            name="address"
            className="w-full px-3 py-2 border rounded"
          ></textarea>
        </div>
        <div className="mb-4">
          <label className="block text-gray-700">Summary</label>
          <input
            type="text"
            name="summary"
            className="w-full px-3 py-2 border rounded"
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700">Website</label>
          <input
            type="text"
            name="website"
            className="w-full px-3 py-2 border rounded"
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700">Linkedin</label>
          <input
            type="text"
            name="linkedin"
            className="w-full px-3 py-2 border rounded"
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700">Github</label>
          <input
            type="text"
            name="github"
            className="w-full px-3 py-2 border rounded"
          />
        </div>
        <button
          type="submit"
          className="bg-purple-600 text-white py-2 px-4 rounded"
        >
          Save
        </button>
      </form>
    </div>
  );
};

export default PersonalDetails;
