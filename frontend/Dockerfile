# Use Node.js 20 Alpine as base image
FROM node:20-alpine

WORKDIR /app

# Install dependencies - only copy package.json first
COPY package.json ./
RUN npm install

# Copy application code
COPY . .

# Build the application
RUN npm run build

# Expose port
EXPOSE 3000

# Start the application
CMD ["npm", "start"] 