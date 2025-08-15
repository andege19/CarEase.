CarEase  
On-Demand Car Servicing Platform  

Project Description:  Web-based solution for booking, tracking, and managing car washing, detailing, tinting, and mechanical services in Nairobi. Solves fragmentation, pricing opacity, and wait times via real-time GPS, AI diagnostics, and M-Pesa/Stripe payments.  

Target Users:  
- Individual vehicle owners  
- Fleet managers  
- Service providers  

Team Members:
Rushil Bhudia - (rushilbhd)
Alice. D. Ndege - (andege19)
Nyalim Kuoth - (24-nyalim)
Alvin Rodney Orina - (aorina915)


 Project Timeline
| Milestone | Description                   | Deadline |
|-----------|-------------------------------|----------|
| Week 5    | Market Research & Setup       | Completed|
| Week 6–10 | Backend & Frontend MVP        | Ongoing  |
| Week 10-11| Testing & Feedback Loops      | Soon     |
| Week 12   | Deployment & Report Submission| Soon     |

Project Board
[Click here to view GitHub Project Board](https://github.com/andege19/CarEase.)

Data Gathering Google Docs link:
https://docs.google.com/forms/d/14pLpU-tV-NooywPylxsTyDyjCrxPeJx2Fbpk5KaZvpA/edit?pli=1#responses

Code of Conduct

Our Pledge

We as members, contributors, and leaders pledge to make participation in our project and our community a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, sex characteristics, gender identity and expression, level of experience, education, socio-economic status, nationality, personal appearance, race, religion, or sexual identity and orientation.

Our Standards

- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable behavior and are expected to take appropriate and fair corrective action in response to any instances of unacceptable behavior.

Scope

This Code of Conduct applies both within project spaces and in public spaces when an individual is representing the project or its community.

Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by contacting the project team at [rodneyalvin4@gmail.com]. All complaints will be reviewed and investigated promptly and fairly.

## Features
- View different services offered
- Book appointments for services 
- View and manage appointments
- Pay for services using M-Pesa 
- Service progress tracking
- Email notifications

## Technologies Used
- **Backend**: Flask (Python)
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript
- **Payment Integration**: M-Pesa (via Daraja API)
- **Email Notifications**: SMTP2Go
- **UI Components**: Mantine 
- **Version Control**: Git
- **Deployment**: Ngrok for local development and testing of the Daraja API integration

## Requirements
- Python 3.x
- Flask
- SQLite
- ngrok for daraja api integration


# Project Structure

```
project/
├── api/
│   ├── __init__.py
│   ├── appointments.py
│   ├── booking.py
│   ├── contact.py
│   ├── daraja.py
│   ├── tracking.py
│   ├── users.py
│   └── util.py
├── db/
│   ├── __init__.py
│   ├── util/
│   │   ├── create.py
│   │   ├── drop.py
│   │   ├── insert.py
│   └── carease.db
│   └── initialize.py
├── misc/
│   ├── __init__.py
│   ├── helpers.py
│   └── constants.py
├── static/
│   ├── css/
│   ├── js/
│   └── img/
│   └── lib/
│   └── scss/
├── templates/
│   ├── 404.html
│   └── index.html
│   └── about.html
│   └── contact.html
│   └── progress.html
│   └── services.html
│   └── tracking.html
├── views/
│   ├── __init__.py
│   ├── index.py
│   └── about.py
│   └── contact.py
│   └── progress.py
│   └── services.py
│   └── tracking.py
├── app.py
├── requirements.txt
├── README.md
```
## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/andege19/CarEase.
    cd CarEase.
    ```
2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
3. Activate the virtual environment:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```
4. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
5. Initialize the database:
    ```bash
    python db/initialize.py
    ```
6. Run the application:
    ```bash
    python app.py
    ```
7. Access the application in your web browser at `http://localhost:[PORT]`, where `[PORT]` is the port number specified in `app.py`.


