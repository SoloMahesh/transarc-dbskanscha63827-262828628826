import re

with open('index.html', 'r') as f:
    content = f.read()

# Make form container more responsive (p-6 on mobile, p-8 on md)
content = content.replace(
    'class="bg-surface-container-low border border-outline-variant/30 rounded-3xl p-8 shadow-[0_20px_50px_rgba(0,0,0,0.1)] dark:shadow-[0_20px_50px_rgba(0,0,0,0.5)] relative overflow-hidden h-full flex flex-col justify-center"',
    'class="bg-surface-container-low border border-outline-variant/30 rounded-3xl p-6 md:p-10 shadow-[0_20px_50px_rgba(0,0,0,0.1)] dark:shadow-[0_20px_50px_rgba(0,0,0,0.5)] relative overflow-hidden h-full flex flex-col justify-center"'
)

# Make map responsive height
content = content.replace(
    'class="h-[200px] w-full rounded-2xl overflow-hidden shadow-inner border border-outline-variant/20"',
    'class="h-[250px] md:h-[300px] w-full rounded-2xl overflow-hidden shadow-inner border border-outline-variant/20"'
)

# Make the grid gap responsive
content = content.replace(
    'class="max-w-container-max mx-auto px-6 md:px-margin-desktop grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-16"',
    'class="max-w-container-max mx-auto px-6 md:px-margin-desktop grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-20"'
)

# Ensure the submit button matches the original naming (Submit Inquiry) and looks super consistent
content = content.replace(
    'Request Estimate <span class="material-symbols-outlined text-sm">arrow_forward</span>',
    'Submit Inquiry <span class="material-symbols-outlined text-sm">arrow_forward</span>'
)

# Fix label consistency to match the old form (Name, Company, Email, Project Details) 
# I will rename "Full Name" to "Name", "Approx. Area" to "Company/Org" to match B2B logic better, or just keep them clean.
content = content.replace('Full Name</label>', 'Name</label>')
content = content.replace('Phone Number *</label>', 'Phone</label>')
content = content.replace('Approx. Area</label>', 'Area Size</label>')

with open('index.html', 'w') as f:
    f.write(content)
