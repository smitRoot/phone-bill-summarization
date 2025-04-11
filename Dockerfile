# Use the official Python image
FROM python:3.9

# Set the working directory
WORKDIR /app


COPY requirements.txt /app/

# RUN pip install streamlit bcrypt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY . /app

# Install dependencies


# Expose the default Streamlit port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "stream.py", "--server.port=8501", "--server.address=0.0.0.0"]
