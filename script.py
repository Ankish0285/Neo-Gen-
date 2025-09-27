# Create comprehensive data for the enhanced Neogen platform with latest updates

import json
from datetime import datetime, timedelta

# Latest Government Internship Notifications and Updates (2025)
latest_notifications = [
    {
        "id": 1,
        "title": "PM Internship Scheme 2025 - Extended Deadline",
        "message": "Application deadline extended to April 22, 2025. Over 1 lakh internship opportunities available across 730 districts with ₹6,000 monthly stipend.",
        "type": "urgent",
        "category": "deadline",
        "date": "2025-04-14",
        "link": "https://www.pminternship.mca.gov.in/",
        "icon": "calendar",
        "priority": "high"
    },
    {
        "id": 2,
        "title": "MEA Internship 2025-26 Term I Notice Released",
        "message": "Ministry of External Affairs has announced the timeline for MEA Internship Program 2025 Term I. Applications opening soon with ₹10,000 monthly honorarium.",
        "type": "new",
        "category": "opportunity",
        "date": "2025-02-20",
        "link": "https://internship.mea.gov.in/internship",
        "icon": "globe",
        "priority": "high"
    },
    {
        "id": 3,
        "title": "MeitY Technical Internship Programme 2025",
        "message": "Ministry of Electronics & IT announces Technical Internship Programme 2025. Last date for applications: June 15, 2025.",
        "type": "new",
        "category": "tech",
        "date": "2025-01-04",
        "link": "https://www.meity.gov.in/",
        "icon": "laptop",
        "priority": "medium"
    },
    {
        "id": 4,
        "title": "NITI Aayog Monthly Application Window",
        "message": "NITI Aayog internship applications are open from 1-10 of every month. Apply now for policy research opportunities.",
        "type": "recurring",
        "category": "policy",
        "date": "2025-09-25",
        "link": "http://niti.gov.in/internship",
        "icon": "briefcase",
        "priority": "medium"
    },
    {
        "id": 5,
        "title": "NALSA Internship Programme 2025",
        "message": "National Legal Services Authority has announced internship opportunities for law students. Check eligibility and apply.",
        "type": "new",
        "category": "legal",
        "date": "2025-03-31",
        "link": "https://nalsa.gov.in/internship-programme-2025/",
        "icon": "scale",
        "priority": "medium"
    }
]

# Enhanced Government Partners for Footer
government_partners = {
    "central_ministries": [
        {
            "name": "Ministry of Electronics & IT (MeitY)",
            "logo": "meity-logo.png",
            "website": "https://www.meity.gov.in",
            "programs": ["Digital India Internship", "Technical Internship Programme"]
        },
        {
            "name": "NITI Aayog",
            "logo": "niti-logo.png", 
            "website": "https://niti.gov.in",
            "programs": ["Policy Research Internship", "Data Analytics Program"]
        },
        {
            "name": "Ministry of External Affairs",
            "logo": "mea-logo.png",
            "website": "https://mea.gov.in",
            "programs": ["Diplomacy Internship", "Foreign Policy Research"]
        },
        {
            "name": "ISRO",
            "logo": "isro-logo.png",
            "website": "https://www.isro.gov.in",
            "programs": ["Space Technology Internship", "Satellite Engineering"]
        }
    ],
    "implementing_agencies": [
        {
            "name": "AICTE",
            "logo": "aicte-logo.png",
            "website": "https://internship.aicte-india.org",
            "programs": ["Technical Education Internships"]
        },
        {
            "name": "Skill India Digital",
            "logo": "skill-india-logo.png",
            "website": "https://www.skillindiadigital.gov.in",
            "programs": ["Skill Development Programs"]
        },
        {
            "name": "National Career Service",
            "logo": "ncs-logo.png",
            "website": "https://www.ncs.gov.in",
            "programs": ["Career Guidance", "Job Matching"]
        }
    ],
    "development_partners": [
        {
            "name": "UNDP India",
            "logo": "undp-logo.png",
            "website": "https://www.undp.org/india",
            "programs": ["SDG Implementation", "Development Partnership"]
        },
        {
            "name": "India-UN Development Partnership Fund",
            "logo": "india-un-logo.png", 
            "website": "https://unsouthsouth.org/indiaunfund/",
            "programs": ["$150M Development Fund", "South-South Cooperation"]
        }
    ]
}

# Enhanced Resource Guides with Better Structure
resource_guides = {
    "getting_started": {
        "title": "Getting Started Guide",
        "description": "Complete beginner's guide to finding and applying for government internships",
        "sections": [
            {
                "title": "Understanding Government Internships",
                "content": "Learn about different types of government internships, eligibility criteria, and benefits",
                "duration": "5 min read",
                "difficulty": "Beginner"
            },
            {
                "title": "Creating Your Profile",
                "content": "Step-by-step guide to setting up your Neogen profile for maximum visibility",
                "duration": "10 min read", 
                "difficulty": "Beginner"
            },
            {
                "title": "Navigation Tutorial",
                "content": "Interactive tour of the platform features and how to use them effectively",
                "duration": "15 min",
                "difficulty": "Beginner"
            }
        ]
    },
    "application_process": {
        "title": "Application Process Mastery",
        "description": "Master the art of government internship applications",
        "sections": [
            {
                "title": "Research & Preparation",
                "content": "How to research organizations, understand requirements, and prepare applications",
                "duration": "20 min read",
                "difficulty": "Intermediate"
            },
            {
                "title": "Resume Optimization",
                "content": "Government-specific resume writing tips and ATS optimization strategies",
                "duration": "25 min read",
                "difficulty": "Intermediate"
            },
            {
                "title": "Application Tracking",
                "content": "Using the dashboard to track applications and follow up effectively",
                "duration": "10 min read",
                "difficulty": "Beginner"
            }
        ]
    },
    "interview_preparation": {
        "title": "Interview Success Strategy",
        "description": "Comprehensive guide to acing government internship interviews",
        "sections": [
            {
                "title": "Common Interview Questions",
                "content": "150+ government internship interview questions with sample answers",
                "duration": "45 min read",
                "difficulty": "Advanced"
            },
            {
                "title": "Virtual Interview Tips",
                "content": "Technology setup, etiquette, and best practices for online interviews",
                "duration": "15 min read",
                "difficulty": "Intermediate"
            },
            {
                "title": "Post-Interview Follow-up",
                "content": "Professional follow-up strategies and thank you note templates",
                "duration": "10 min read",
                "difficulty": "Beginner"
            }
        ]
    }
}

# ATS Score Improvement Tips
ats_improvement_tips = {
    "formatting": [
        "Use standard section headings (Experience, Education, Skills)",
        "Choose ATS-friendly fonts like Arial, Calibri, or Times New Roman",
        "Avoid images, graphics, and complex formatting",
        "Use consistent bullet points and spacing",
        "Save resume as both PDF and Word document"
    ],
    "keywords": [
        "Include relevant keywords from job descriptions",
        "Use industry-specific terminology naturally",
        "Add action verbs like 'managed', 'developed', 'implemented'",
        "Include both full forms and abbreviations (e.g., 'AI' and 'Artificial Intelligence')",
        "Integrate skills mentioned in internship requirements"
    ],
    "content": [
        "Quantify achievements with numbers and percentages",
        "Include relevant coursework and projects",
        "Add certifications and technical skills",
        "Write a compelling professional summary",
        "Tailor content to each internship application"
    ],
    "completeness": [
        "Include complete contact information",
        "Add LinkedIn profile and professional email",
        "List all relevant education details",
        "Include relevant work experience or projects",
        "Add language proficiencies if applicable"
    ]
}

# Multi-step form structure for better UX
form_structure = {
    "steps": [
        {
            "step": 1,
            "title": "Personal Information",
            "description": "Basic details to get started",
            "fields": ["Full Name", "Email", "Phone", "Date of Birth", "Address"],
            "estimated_time": "2 minutes"
        },
        {
            "step": 2, 
            "title": "Academic Background",
            "description": "Your educational qualifications",
            "fields": ["Degree", "University", "Year of Study", "CGPA/Percentage", "Specialization"],
            "estimated_time": "3 minutes"
        },
        {
            "step": 3,
            "title": "Skills & Experience", 
            "description": "Your technical and soft skills",
            "fields": ["Technical Skills", "Soft Skills", "Certifications", "Projects", "Experience"],
            "estimated_time": "5 minutes"
        },
        {
            "step": 4,
            "title": "Document Upload",
            "description": "Upload your resume and certificates",
            "fields": ["Resume", "Academic Transcripts", "Certificates", "Cover Letter"],
            "estimated_time": "3 minutes"
        },
        {
            "step": 5,
            "title": "Preferences",
            "description": "Your internship preferences",
            "fields": ["Preferred Locations", "Departments", "Duration", "Start Date", "Remote/Onsite"],
            "estimated_time": "2 minutes"
        }
    ],
    "total_estimated_time": "15 minutes",
    "completion_tracking": True,
    "save_progress": True,
    "conditional_logic": True
}

# Print summary
print("Enhanced Neogen Platform Data Created Successfully!")
print(f"Latest Notifications: {len(latest_notifications)}")
print(f"Government Partners: {len(government_partners['central_ministries']) + len(government_partners['implementing_agencies']) + len(government_partners['development_partners'])}")
print(f"Resource Guide Sections: {len(resource_guides)}")
print(f"Form Steps: {len(form_structure['steps'])}")
print(f"ATS Improvement Categories: {len(ats_improvement_tips)}")

# Create JSON for the application
enhanced_data = {
    "notifications": latest_notifications,
    "partners": government_partners,
    "resources": resource_guides,
    "ats_tips": ats_improvement_tips,
    "form_structure": form_structure
}

print("\nData structure ready for enhanced Neogen application!")