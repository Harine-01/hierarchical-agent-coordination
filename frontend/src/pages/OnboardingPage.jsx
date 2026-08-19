import { useState } from "react";

function OnboardingPage() {
  const [formData, setFormData] = useState({
    employee_name: "",
    employee_id: "",
    department: "",
    designation: "",
    joining_date: "",
    email: "",
    phone: "",
    manager: "",
  });

  const [message, setMessage] = useState("");

  const handleChange = (e) => {
    const { name, value } = e.target;

    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (
      !formData.employee_name ||
      !formData.employee_id ||
      !formData.department ||
      !formData.designation ||
      !formData.joining_date ||
      !formData.email
    ) {
      setMessage("Please fill all required fields.");
      return;
    }

    setMessage("Form submitted successfully!");

    console.log("Form Data:", formData);
  };

  return (
    <div>
      <h1>Employee Onboarding</h1>

      <form onSubmit={handleSubmit}>
        <label>Employee Name</label>
        <input
          type="text"
          name="employee_name"
          value={formData.employee_name}
          onChange={handleChange}
        />

        <br /><br />

        <label>Employee ID</label>
        <input
          type="text"
          name="employee_id"
          value={formData.employee_id}
          onChange={handleChange}
        />

        <br /><br />

        <label>Department</label>
        <input
          type="text"
          name="department"
          value={formData.department}
          onChange={handleChange}
        />

        <br /><br />

        <label>Designation</label>
        <input
          type="text"
          name="designation"
          value={formData.designation}
          onChange={handleChange}
        />

        <br /><br />

        <label>Joining Date</label>
        <input
          type="date"
          name="joining_date"
          value={formData.joining_date}
          onChange={handleChange}
        />

        <br /><br />

        <label>Email</label>
        <input
          type="email"
          name="email"
          value={formData.email}
          onChange={handleChange}
        />

        <br /><br />

        <label>Phone</label>
        <input
          type="tel"
          name="phone"
          value={formData.phone}
          onChange={handleChange}
        />

        <br /><br />

        <label>Manager</label>
        <input
          type="text"
          name="manager"
          value={formData.manager}
          onChange={handleChange}
        />

        <br /><br />

        <button type="submit">
          Submit Onboarding
        </button>
      </form>

      {message && <p>{message}</p>}
    </div>
  );
}

export default OnboardingPage;