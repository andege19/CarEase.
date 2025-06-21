Software Requirements Document (SRD) for CarEase Platform
Version 1.0

SECTION 1: Introduction to Requirements Engineering
Introduction

Project Overview
CarEase is an innovative web-based platform designed to revolutionize the car servicing, detailing, tinting, and maintenance industry in Kenya. It provides on-demand car-related services at the customer’s chosen location, leveraging digital solutions such as online booking, real-time service provider tracking, secure digital payments, and a customer review system. CarEase aims to eliminate inefficiencies in traditional car servicing by ensuring transparency, accessibility, eco-friendly service options, and high-quality customer experiences

Purpose
The purpose of CarEase is to modernize the car servicing sector in Kenya by providing a centralized, technology-driven solution that addresses the pain points of traditional service models: limited accessibility, long wait times, inconsistent pricing, lack of transparency, and poor service quality. The platform seeks to empower both customers and service providers through streamlined processes, standardized pricing, verified reviews, and sustainable practices

Scope
CarEase will offer a comprehensive suite of services including car washing, detailing, tinting, and general servicing. The platform will cater to urban, suburban, and rural customers, providing mobile and on-demand services. Key features include:

Online appointment scheduling and automated booking

Real-time tracking of service providers

Secure, cashless payments

Customer review and rating system

AI-powered diagnostics and predictive maintenance reminders

Eco-friendly service options (e.g., water-efficient washing, biodegradable products)

Service provider onboarding and management portal



SECTION 2: Stakeholder Analysis

A thorough stakeholder analysis ensures that all parties affected by or interacting with CarEase are identified, understood, and their needs addressed.

Primary Stakeholders

Vehicle Owners/Customers: Individuals seeking convenient, reliable, and transparent car servicing. Their needs include ease of booking, trust in service quality, clear pricing, and environmental responsibility.

Service Providers: Car wash operators, detailers, mechanics, and tinting specialists who will register on the platform. They require fair access to customers, transparent payment processes, and a system for managing appointments and reviews.

Platform Administrators: Responsible for managing the platform, onboarding service providers, handling disputes, ensuring compliance, and maintaining system integrity.

Investors/Owners: Stakeholders interested in the platform’s profitability, scalability, and market share.

Secondary Stakeholders

Regulatory Bodies: Such as the National Environment Management Authority (NEMA) and Ministry of Transport, concerned with compliance to environmental and industry standards.

Insurance Companies: Potential partners for value-added services like insurance verification or claims processing.

Third-Party Technology Providers: Payment gateways, SMS/email notification services, and AI/IoT solution vendors.

Local Communities: Impacted by environmental practices and job creation.

Stakeholder Needs and Influence

Customers demand convenience, transparency, and reliability.

Service providers seek increased business, fair reviews, and prompt payments.

Regulators require compliance with environmental and business standards.

Investors focus on growth, ROI, and market differentiation.



SECTION 3: Data Gathering & Market Research as Inputs to Requirements

Inputs
The requirements are informed by extensive market research, data gathering, and analysis of industry trends, customer pain points, and competitor offerings.

Market Research Details

The car servicing industry in Kenya is fragmented, with most providers relying on manual processes.

Urbanization and vehicle ownership are rising, yet service accessibility remains limited, especially outside major cities.

Traditional service centers often lack standardized pricing, leading to customer distrust and dissatisfaction.

Environmental sustainability is a growing concern, with high water usage and chemical waste from conventional car washes

Data Collection Techniques and Summary

Primary Research:

Interviews: Conducted with car owners, service providers, and industry experts to understand pain points and expectations.

Questionnaires: Distributed to a broad demographic to gather quantitative data on frequency of car servicing, preferred service types, booking challenges, and willingness to pay for convenience and eco-friendly options (see Google Forms data).

Field Observations: Visits to car washes and garages to observe workflows, wait times, and customer interactions.

Workshops: Collaborative sessions with stakeholders to brainstorm features and validate requirements.

Secondary Research:

Market Reports: Analysis of the automotive servicing sector in Kenya and global trends in digital transformation.

Academic Articles: Insights into the impact of digital platforms on service delivery and customer satisfaction.

Competitor Analysis: Review of local and international platforms (e.g., YourMechanic, Fixter) to identify best practices and gaps.

Reviews: Study of customer feedback on existing services to identify recurring issues and desired features

Key findings from the data include:

73% of car owners spend more than two hours at service stations for routine maintenance.

92% of respondents reported being overcharged at least once.

There is high demand for mobile, on-demand, and eco-friendly car servicing options.



SECTION 4: System Overview

CarEase is a web-based platform designed to connect car owners with trusted service providers for washing, detailing, tinting, and maintenance. The system will have the following core modules:


-Customer Portal:

User registration and profile management

Service selection and scheduling

Real-time tracking of service provider arrival

Secure online payment processing

Ratings and reviews submission


-Service Provider Portal:

Registration and verification

Service listing management

Appointment scheduling and calendar sync

Real-time navigation and status updates

Earnings dashboard and payout management


-Admin Dashboard:

User and provider management

Dispute resolution

Analytics and reporting

Compliance and quality control

-AI & IoT Integration:

Diagnostics for predictive maintenance

Automated reminders for scheduled services

IoT-enabled tracking for service provider location

-Eco-Friendly Features:

Option to select green cleaning services

Tracking of water and chemical usage for compliance

The system will be accessible via web browsers and optimized for mobile use, ensuring broad accessibility.

Excluded Features
Major mechanical repairs (engine overhauls, transmission replacements).  
Vehicle towing/roadside assistance.  
Car sales, leasing, or rentals.  
Offline functionality.  
Insurance claim processing.  
Advanced OBD diagnostics (beyond basic IoT).  
Multi-currency support (initial release: KES only).  
Voice command integration (e.g., Siri/Alexa).  


Key Workflows:
Booking: User selects service → Chooses time/location → Receives upfront quote.

Service Execution: Technician tracked via GPS → AI diagnostics generate maintenance report.

Payment: Secure transaction → Digital invoice → User rating.


Architecture
Frontend: React.js (responsive UI, real-time updates).

Backend: Node.js + Express.js (API routing, payment processing).

Database: MongoDB (scalable JSON storage).

Cloud: AWS EC2/S3 (auto-scaling, redundancy).

APIs: Google Maps (GPS), M-Pesa/Stripe (payments), TensorFlow (AI).



SECTION 5: Functional Requirements

ID	Description	Rationale	Acceptance Criteria
FR-01	The system shall allow users to register and create a profile.	Enables personalized service and tracking.	Users can register, receive confirmation, and log in.
FR-02	The system shall enable customers to book car services online.	Streamlines appointment scheduling and reduces wait times.	Users can select service, time, and location.
FR-03	The system shall provide real-time tracking of service providers.	Increases transparency and trust.	Users see provider ETA and live location.
FR-04	The system shall support secure digital payments.	Ensures safe, cashless transactions.	Payments processed via M-Pesa, credit/debit card, etc.
FR-05	The system shall allow customers to rate and review service providers.	Promotes accountability and service quality.	Users can submit ratings and written reviews.
FR-06	The system shall provide a dashboard for service providers to manage bookings and payments.	Empowers providers to track business and earnings.	Providers access dashboard with booking/payment info.
FR-07	The system shall offer eco-friendly service options.	Supports environmental sustainability.	Users can choose green services; usage is tracked.
FR-08	The system shall send automated reminders for scheduled services.	Improves customer retention and vehicle maintenance.	Users receive notifications before appointments.
FR-09	The system shall allow admin to onboard, verify, and manage service providers.	Ensures only qualified providers join the platform.	Admin can approve/reject and monitor providers.
FR-10	The system shall generate analytics and reports for admin.	Supports business decision-making and compliance.	Admin accesses detailed usage and performance reports.



SECTION 6: Non-Functional Requirements

ID	Category	Description	Acceptance Criteria
NFR-01	Security	The system shall support end-to-end AES encryption for all data in transit.	All traffic is encrypted; verified by audit.
NFR-02	Availability	The system shall maintain 99.9% uptime during peak hours.	Uptime logs show <0.1% downtime in peak periods.
NFR-03	Usability	The system shall provide an accessible UI, conforming to WCAG 2.1 AA standards.	Accessibility audit passes all WCAG 2.1 AA tests.
NFR-04	Performance	The system shall load the main dashboard within 2 seconds for 95% of users.	Performance logs confirm compliance.
NFR-05	Scalability	The system shall handle 10,000 concurrent users without degradation.	Load tests confirm no drop in performance.
NFR-06	Compliance	The system shall comply with NEMA and data protection regulations in Kenya.	Compliance audit reports no violations.
NFR-07	Maintainability	The system codebase shall follow industry-standard documentation and modular design.	Code review confirms documentation and modularity



SECTION 7: Assumptions and Constraints
Assumptions

Reliable internet access is available to customers and service providers in target regions.

Service providers have smartphones or devices compatible with the platform.

Regulatory environment remains favorable to digital platforms and mobile payments.

Customers are willing to adopt cashless payment methods.


Constraints

Integration with third-party payment gateways (e.g., M-Pesa) may be subject to transaction fees and downtime.

Environmental regulations may evolve, requiring updates to eco-friendly service offerings.

Data privacy laws (e.g., Kenya Data Protection Act) must be strictly adhered to.

Competition from emerging or established platforms may impact market share.

Initial onboarding of service providers may require extensive verification and training.




SECTION 8: Acceptance Criteria

Requirement ID	Acceptance Criteria
FR-01	User can register, receive confirmation email/SMS, and log in successfully.
FR-02	User can select service, date/time, location, and receive booking confirmation.
FR-03	User can view real-time location of assigned service provider on a map.
FR-04	User can complete payment transaction securely and receive receipt.
FR-05	User can submit a rating (1-5 stars) and a written review after service completion.
FR-06	Service provider can view/manage bookings, mark jobs as complete, and see payment status.
FR-07	User can select eco-friendly service option; system tracks and reports usage.
FR-08	User receives notification (email/SMS/push) 24 hours and 1 hour before scheduled service.
FR-09	Admin can approve/reject provider applications and view provider performance metrics.
FR-10	Admin dashboard displays real-time analytics on bookings, revenue, and customer feedback.



SECTION 9: Functional Requirements Traceability Matrix
Linked to GitHub Project Board: CarEase Functional Traceability
Requirement ID	GitHub Issue #	Developer Assigned	Status		Test Case Ref	Verified
FR-01		#1		@alice-dev		To Do		TC-01		No
FR-02		#2		@all-dev			To Do		TC-02		No
FR-03		#3		@rushil-dev		To Do		TC-03		No
FR-04		#4		@alvin-dev		To Do		TC-04		No
FR-05		#5		@rushil-dev		To Do		TC-05		No
FR-06		#6		@alice-dev		To Do		TC-06		No
FR-07		#7		@alvin-dev		To Do		TC-07		No
FR-08		#8		@rushil-dev		To Do		TC-08		No
FR-09		#9		@nyalim-dev		To Do		TC-09		No
FR-10		#10		@nyalim-dev		To Do		TC-10		No


10. Regulatory Compliance
Data Protection (KDPA 2019):

Role-based access control (RBAC).

User data deletion within 72 hours of request.

Financial (PCI-DSS):

Tokenization of card details; no raw payment data storage.

Environmental (NEMA):

Wastewater recycling systems for partner garages.

Tax (KRA):

Automated VAT reporting in service provider dashboards.

Appendix A: References
Kenya Data Protection Act (2019).

NEMA Waste Management Guidelines (2022).

PCI-DSS v3.2.1 Security Standard.

Green, P., & Patel, R. (2023). Digital Transformation in Automotive Services.

KNBS Vehicle Ownership Report (2023).

Appendix B: Glossary
KDPA: Kenya Data Protection Act.

PCI-DSS: Payment Card Industry Data Security Standard.

NEMA: National Environment Management Authority (Kenya).

STK Push: SIM ToolKit Push (M-Pesa payment method).

Prepared By: Product Management Team
Distribution: Developers, Stakeholders, Regulatory Auditors


