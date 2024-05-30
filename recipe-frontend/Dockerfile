# Dockerfile for Vue frontend
FROM node:14

# Set working directory
WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm install

# Copy project
COPY . .

# Expose port 8080
EXPOSE 8080

# Run the application
CMD ["npm", "run", "serve"]