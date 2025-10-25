# Google Analytics 4 (GA4) Setup Guide

## Overview
This Flask application has been enhanced with comprehensive Google Analytics 4 (GA4) performance analytics tracking across all page variants.

## Setup Instructions

### 1. Get Your GA4 Measurement ID
1. Go to [Google Analytics](https://analytics.google.com/)
2. Create a new GA4 property or use an existing one
3. Go to Admin > Data Streams > Web
4. Copy your Measurement ID (format: G-XXXXXXXXXX)

### 2. Configure Environment Variables
Set the following environment variable before running the application:

```bash
export GA4_MEASUREMENT_ID="G-XXXXXXXXXX"
```

Or create a `.env` file in your project root:
```
GA4_MEASUREMENT_ID=G-XXXXXXXXXX
```

### 3. Run the Application
```bash
python app.py
```

## Analytics Features Implemented

### Page Tracking
- **Page Views**: Automatic tracking of all page visits
- **Page Variants**: Tracks which design variant users visit (original, colors, sizes, spacing, typography)
- **Time on Page**: Measures how long users spend on each page

### User Interaction Tracking
- **Button Clicks**: Tracks clicks on CTA buttons
- **Navigation Clicks**: Tracks navigation between different variants
- **Feature Interactions**: Tracks hover and click events on feature cards
- **External Link Clicks**: Tracks outbound link clicks

### Performance Monitoring
- **Page Load Time**: Tracks how long pages take to load
- **DOM Content Loaded**: Measures DOM processing time
- **Core Web Vitals**: Basic performance metrics
- **Scroll Depth**: Tracks how far users scroll (25%, 50%, 75%, 100%)

### Engagement Tracking
- **User Engagement Time**: Tracks active user engagement
- **Scroll Behavior**: Monitors scrolling patterns
- **Feature Hover**: Tracks which features users interact with

## GA4 Events Being Tracked

| Event Name | Category | Description |
|------------|----------|-------------|
| `page_view` | - | Automatic page view tracking |
| `cta_click` | engagement | Button clicks |
| `navigation_click` | navigation | Navigation menu clicks |
| `feature_hover` | engagement | Feature card hovers |
| `feature_click` | engagement | Feature card clicks |
| `scroll_depth` | engagement | Scroll depth milestones |
| `time_on_page` | engagement | Time spent on page |
| `user_engagement` | engagement | Active engagement time |
| `page_performance` | performance | Page load metrics |
| `external_link_click` | outbound | External link clicks |

## Custom Parameters

Each event includes custom parameters:
- `page_variant`: Which design variant (original, colors, sizes, spacing, typography)
- `event_category`: Event categorization
- `event_label`: Specific element identifier
- `value`: Numeric value for the event

## Viewing Analytics Data

1. Go to your Google Analytics dashboard
2. Navigate to Reports > Engagement > Events
3. Use the "Event name" filter to view specific events
4. Create custom reports to analyze performance across different page variants

## A/B Testing Capabilities

The implementation supports A/B testing by tracking:
- Which page variants users visit
- Performance metrics for each variant
- User engagement patterns across variants
- Conversion rates for different designs

## Performance Considerations

- GA4 tracking is loaded asynchronously to avoid blocking page load
- Events are batched and sent efficiently
- No impact on page load performance
- GDPR-compliant implementation (no personal data collected)

## Troubleshooting

### GA4 Not Tracking
1. Verify your Measurement ID is correct
2. Check browser console for JavaScript errors
3. Ensure the environment variable is set correctly
4. Test in incognito mode to avoid ad blockers

### Missing Events
1. Check that JavaScript is enabled
2. Verify the gtag function is available
3. Check browser console for tracking errors

## Development vs Production

- **Development**: Set `GA4_MEASUREMENT_ID` to a test property
- **Production**: Use your production GA4 property ID
- **Testing**: Use Google Analytics DebugView for real-time event testing
