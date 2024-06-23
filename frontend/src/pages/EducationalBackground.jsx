import React from "react";

const PersonalDetails = () => {
  return (
    <div>
      <h2 className="text-2xl font-semibold mb-4">Educational Background</h2>

      <form>
        <div className="mb-4">
          <label className="block text-gray-700">Profile</label>
          <input
            type="text"
            name="profile"
            className="w-full px-3 py-2 border rounded"
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700">Institution</label>
          <input
            type="text"
            name="institution"
            className="w-full px-3 py-2 border rounded"
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700">Degree</label>
          <input
            type="text"
            name="degree"
            className="w-full px-3 py-2 border rounded"
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700">Field of Study</label>
          <input
            type="text"
            name="field_of_study"
            className="w-full px-3 py-2 border rounded"
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700">Start Date</label>
          <input
            type="date"
            name="start_date"
            className="w-full px-3 py-2 border rounded"
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700">End Date</label>
          <input
            type="text"
            name="end_date"
            className="w-full px-3 py-2 border rounded"
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700">Grade</label>
          <input
            type="text"
            name="grade"
            className="w-full px-3 py-2 border rounded"
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700">Description</label>
          <input
            type="text"
            name="description"
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
