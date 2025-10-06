# Hind Guru Academy - MBBS Abroad Consultancy Platform

## Overview

Hind Guru Academy is a Django-based web application serving as an educational consultancy platform for Indian students seeking MBBS admissions abroad. The platform provides comprehensive information about international medical universities, scholarship opportunities, admission services, and counseling for students pursuing medical education in countries like Bangladesh, Uzbekistan, Kazakhstan, Tajikistan, and others.

**Current Status:** Fully functional website with beautiful animations and responsive design.

**Last Updated:** October 04, 2025

## User Preferences

- Preferred communication style: Simple, everyday language (Hindi/English mix acceptable)
- Focus on visual appeal with animations
- Professional academy-style design

## Recent Changes (October 04, 2025)

- ✅ Built complete Django website from scratch
- ✅ Created 7 main pages: Home, About, Services, Destinations, Scholarships, FAQ, Contact
- ✅ Implemented beautiful gradient animations and scroll effects
- ✅ Added responsive navigation and footer
- ✅ Integrated AOS (Animate On Scroll) library for smooth animations
- ✅ Created interactive FAQ accordions
- ✅ Added animated statistics counters
- ✅ Configured Django workflow running on port 5000

## Project Architecture

### Backend Architecture

**Framework:** Django 5.2.7
- **Structure:** Single "core" app handling all views and URLs
- **Views:** Function-based views for all 7 pages
- **URL Routing:** Clean URL patterns with named routes
- **Database:** SQLite (default Django ORM)
- **Static Files:** Organized in /static/css and /static/js directories
- **Templates:** Template inheritance with base.html

### Frontend Architecture

**Template System:** Django Templates with inheritance
- **Base Template:** `templates/base.html` with navbar and footer
- **Page Templates:** Home, About, Services, Destinations, Scholarships, FAQ, Contact

**CSS Framework:** Bootstrap 5.3.0 (CDN)
**Animation Library:** AOS 2.3.1 (Animate On Scroll)
**Icons:** Font Awesome 6.4.0

**Design System:**
- Custom CSS with gradient themes (purple/violet primary colors)
- Responsive design for all screen sizes
- Smooth animations and transitions
- Interactive hover effects
- Professional color scheme with CSS variables

**Key Features:**
- Animated hero sections with gradient backgrounds
- Scroll-triggered animations on all sections
- Interactive FAQ accordions with smooth transitions
- Animated statistics counters
- Country cards with hover effects
- Feature cards with icon animations
- Responsive navigation with mobile menu
- Back-to-top button
- Social media links in footer

### Pages Structure

1. **Home** (`/`) - Hero section, key features, statistics, destinations preview, services preview
2. **About Us** (`/about/`) - Mission, core principles, achievements, why choose us
3. **Services** (`/services/`) - All 9 services with detailed descriptions, process flow
4. **Destinations** (`/destinations/`) - 4 main countries (Bangladesh, Uzbekistan, Kazakhstan, Tajikistan) + 8 additional destinations
5. **Scholarships** (`/scholarships/`) - ₹1,00,000 scholarship details, SAARC quota information, merit-based options
6. **FAQ** (`/faq/`) - Interactive accordion-style FAQs in 5 categories
7. **Contact** (`/contact/`) - Contact form, office information, Google Maps, social links

### Static Files

**CSS** (`/static/css/style.css`):
- 700+ lines of custom styling
- CSS variables for consistent theming
- Gradient backgrounds and animations
- Responsive media queries
- Hover effects and transitions
- Animation keyframes for various effects

**JavaScript** (`/static/js/main.js`):
- AOS initialization
- Navbar scroll effects
- FAQ accordion functionality
- Animated counter implementation
- Back-to-top button
- Smooth scroll for anchor links

### Content Highlights

**Key Messages:**
- ₹1,00,000 guaranteed scholarship benefit for all students
- Direct university coordination (no middlemen)
- NMC & WHO recognized universities only
- Complete end-to-end support
- Transparent pricing and documentation

**Target Countries:**
- Primary: Bangladesh, Uzbekistan, Kazakhstan, Tajikistan
- Additional: Kyrgyzstan, Egypt, Georgia, Russia, Nepal, Philippines, China, Armenia

### External Dependencies

**Frontend CDN:**
- Bootstrap 5.3.0
- Font Awesome 6.4.0
- AOS 2.3.1

**Backend:**
- Django 5.2.7
- Python 3.11

### Configuration

**Settings:**
- `DEBUG = True` (development)
- `ALLOWED_HOSTS = ['*']`
- Templates directory: `BASE_DIR / 'templates'`
- Static files directory: `BASE_DIR / 'static'`
- Core app installed and configured

**Workflow:**
- Name: Django Server
- Command: `python manage.py runserver 0.0.0.0:5000`
- Port: 5000
- Output: webview

### Security Considerations

**Current Development Settings:**
- Secret key exposed (should use environment variables in production)
- Debug mode enabled (must disable for production)
- ALLOWED_HOSTS accepts all (should restrict in production)

**Future Production Requirements:**
- Environment variable management
- PostgreSQL database
- Static file hosting (AWS S3 / CDN)
- HTTPS configuration
- Contact form backend with email integration

### Testing Status

- ✅ All pages load successfully (200 status)
- ✅ Static files (CSS/JS) serve correctly
- ✅ Navigation links work properly
- ✅ Responsive design verified
- ✅ Animations display correctly
- ✅ Server runs without errors

### Future Enhancements

**Phase 2 Recommendations:**
1. Contact form backend with database storage
2. Email notification system
3. Admin panel for managing inquiries
4. Student authentication portal
5. Blog/news section
6. Multi-language support (Hindi/English toggle)
7. WhatsApp integration
8. Payment gateway integration
9. Document upload functionality
10. Application tracking system

### Deployment Notes

- Currently running on port 5000
- Ready for production deployment after security configurations
- Requires PostgreSQL setup for production
- Static files need CDN configuration
- Domain and SSL certificate needed
