Project Requirements Document: CarEase 
Version:1.0  
 
1. Introduction
1.1 Background
The car servicing industry in Kenya remains largely traditional, characterized by inefficiencies such as long wait times, inconsistent pricing, lack of transparency, and limited accessibility. Despite digital transformations in sectors like ride-hailing (Uber, Bolt) and e-commerce (Jumia), car maintenance services in Nairobi rely on manual processes, fragmented platforms, and physical visits. CarEase addresses these gaps by providing an integrated web-based platform for on-demand car washing, detailing, tinting, and servicing.  

1.2 Problem Statement  
Key challenges in Kenya’s car servicing industry include:  
- Inefficiency: 73% of car owners spend >2 hours at service centers (Automobile Association of Kenya, 2023).  
- Accessibility: Traffic congestion in Nairobi results in 57-minute daily commutes (Kenya Urban Roads Authority, 2022).  
- Transparency: 92% of users report overcharging (Consumer Federation of Kenya, 2023).  
- Environmental Impact: Traditional car washes consume 150–200L of water per vehicle (NEMA, 2022).  
- Fragmentation: No unified platform exists for comprehensive car care.  

1.3 Project Objectives
1.3.1 General Objective 
Design and develop CarEase, a user-centric web platform enabling seamless booking, tracking, and management of car washing, detailing, tinting, and servicing appointments.  

1.3.2 Specific Objectives
1. Design an intuitive UI for simplified service booking.  
2. Integrate real-time GPS tracking for service provider monitoring.  
3. Implement secure digital payments (M-Pesa, cards).  
4. Establish a feedback/rating system for transparency.  
5. Ensure scalability for semi-urban/rural expansion.  
6. Prioritize data security (encryption, GDPR compliance).  
7. Support cross-device compatibility (desktop, mobile).  
8. Enable real-time analytics for service providers.  


2. Scope
2.1 Included Features 
| Feature                    | Description                                                               |
| Web-Based Booking          | Schedule car washing, detailing, tinting, and maintenance online.         |
| Real-Time GPS Tracking     | Track service providers’ locations and estimated arrival times.           |
| Secure Payment Gateway     | Support M-Pesa, cards, bank transfers with PCI-DSS compliance.            |
| Customer Feedback System   | Rate/review services to ensure accountability.                            |
| Automated Notifications    | Appointment confirmations, reminders, and service updates via SMS/email   |
| AI Service Recommendations | Personalized maintenance suggestions based on vehicle history.            |
| Multi-Device Support       | Responsive design for iOS, Android, Windows, and macOS.                   |
| Data Security              | End-to-end encryption, 2FA, and GDPR-compliant data handling.             |
| Scalable Architecture      | Modular design for future IoT/blockchain integration.                     |

2.2 Excluded Features
- Major mechanical repairs (engine overhauls, transmission replacements).  
- Vehicle towing/roadside assistance.  
- Car sales, leasing, or rentals.  
- Offline functionality.  
- Insurance claim processing.  
- Advanced OBD diagnostics (beyond basic IoT).  
- Multi-currency support (initial release: KES only).  
- Voice command integration (e.g., Siri/Alexa).  


3. Significance 
3.1 Benefits to Car Owners
- Convenience: Book services from home/office.  
- Transparency: Upfront pricing and real-time tracking.  
- Proactive Maintenance: AI-driven reminders to prevent breakdowns.  
- Cost Savings: Reduced repair costs through timely servicing.  

3.2 Benefits to Service Providers  
- Efficiency: Automated scheduling reduces idle time.  
- Market Visibility: Access to broader customer base.  
- Data Insights: Analytics on customer trends and performance.  
- Revenue Growth: Optimized booking and cashless payments.  

3.3 Economic & Environmental Impact  
- Job Creation: Opportunities for IT professionals, mechanics, and logistics coordinators.  
- Eco-Friendly Practices: Water-efficient washing, biodegradable products, optimized routes to reduce emissions.  

3.4 Policy Alignment  
- Supports Kenya Vision 2030’s digital economy goals.  
- Compliant with Data Protection Act (2019) and UN SDGs 9 (Industry) and 11 (Sustainable Cities).  



4. Functional Requirements 
| Feature             | User Action                          | System Response                            |
| User Registration   | Sign up via email/phone/social media.| Secure account creation with 2FA.                   |
| Service Booking     | Select service type, time, location. | Real-time availability confirmation.      |         
| Payment Processing  | Choose M-Pesa/card/bank transfer.    | Encrypted transaction; instant invoice generation.  |
| Real-Time Tracking  | View service provider’s live location| ETA updates via Google Maps API.                    |
| Feedback Submission | Rate service (1–5 stars) and add comments| Publish reviews; notify providers for improvement.  |
| Service History     | Access past invoices/service records | Display timeline of services with provider details| 


5. Non-Functional Requirements 
| Category      | Requirement                                                                     |
| Performance   | Response time ≤2 seconds; handle 100K+ concurrent users.                        |
| Scalability   | Cloud-based architecture (AWS/Google Cloud) with auto-scaling.                  |
| Reliability   | 99.9% uptime; automated backups and failover mechanisms.                        |
| Usability     | Intuitive UI (Figma-designed); 95% user satisfaction in UAT.                    |
| Security      | End-to-end encryption, PCI-DSS compliance, OWASP ZAP vulnerability scans.       |
| Maintainability| Modular code (React.js/Node.js); CI/CD pipelines (Jenkins/GitHub Actions).     |



6. System Requirements  
6.1 Hardware Requirements 
|Component      | Minimum                          | Recommended                               |
|Server         | 16GB RAM, 500GB SSD              | 32GB RAM, 1TB NVMe SSD                    |
|Client Device  | Dual-core CPU, 4GB RAM, 64GB storage | Quad-core CPU, 8GB RAM, 128GB storage |
|Network        | 10 Mbps bandwidth                | 50 Mbps + load balancer (AWS ELB)         |

6.2 Software Requirements
|   Component           | Technology Stack                                                  |
|   Frontend            | React.js (responsive PWA)                                         |
|   Backend             | Node.js, Express.js                                               |
|   Database            | MongoDB (NoSQL for flexible data)                                 |
|   APIs                | Google Maps (tracking), M-Pesa/Stripe (payments), TensorFlow (AI) |
|   DevOps              | Docker (containerization), GitHub Actions (CI/CD)                 |
|   OS                  | Ubuntu Server 22.04 LTS (backend)                                 |



7. Stakeholders  
| Stakeholder        | Role                                                                 |
| Car Owners         | Primary users; book services, track providers, submit reviews.       |
| Service Providers  | Mechanics/detailers; manage appointments, receive payments.          |
| System Administrators| Manage user accounts, service provider registrations, analytics.   |
| Developers         | Maintain/upgrade platform; implement security patches.               |
| Government Bodies  | Ensure compliance with data protection (Kenya DPA) and sustainability|


Constraints & Assumptions  
Constraints 
- Budget: \$10,000–\$20,000 for development and initial marketing.  
- Timeline: 6-month development cycle (Agile sprints).  
- Geography: Initial launch limited to Nairobi; semi-urban expansion in Phase 2.  

Assumptions 
- 70% of service providers will adopt digital tools within 6 months.  
- User base growth: 5,000+ active users by Year 1.  
- M-Pesa API integration covers 85% of Kenyan mobile money users.  


9. Risks & Mitigation 
| Risk                         | Mitigation Strategy                                              |
| Service Provider Resistance  | Training workshops; tiered commission models.                    |
| Payment Fraud                | Stripe/M-Pesa fraud detection; SSL/TLS encryption.               |
| System Scalability Issues    | Auto-scaling cloud infrastructure; load testing (JMeter).        |
| Data Breaches                | Regular security audits; GDPR/DPA compliance; 2FA.               |
| Low User Adoption            | Promotional discounts; partnerships with vehicle dealerships.    |



10. Glossary 
- IoT: Internet of Things (e.g., vehicle diagnostics).  
- PCI-DSS: Payment Card Industry Data Security Standard.  
- PWA: Progressive Web App (offline functionality).  
- UAT:User Acceptance Testing.  
- GDPR:General Data Protection Regulation (compliance).  

