FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the necessary files to the working directory
COPY requirements.txt .
COPY app.py .
COPY savings_opportunities_tab.py .
COPY usage_comparison_chart_tab.py .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the necessary port
EXPOSE 8000

# Start the Gunicorn server with the Dash app
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:server"]