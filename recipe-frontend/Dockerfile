# Dockerfile for Vue frontend

# Use the official Node.js image from the Docker Hub
FROM node:14

# Set the working directory
WORKDIR /app

# Copy the entire project into the container
COPY recipe-frontend /app/

# Install any dependencies
RUN npm install

# Expose the port the app runs on
EXPOSE 8080

# Run the application
CMD ["npm", "run", "serve"]