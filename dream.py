from flask import Flask, render_template, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Route: Serve the main landing page
@app.route('/')
def home():
    # Flask looks in the 'templates' folder for this file
    return render_template('index.html')

# Route: Example API endpoint for an email newsletter
@app.route('/api/subscribe', methods=['POST'])
def subscribe():
    try:
        # Get JSON data sent from the frontend
        data = request.get_json()
        email = data.get('email')
        
        if not email:
            return jsonify({"error": "Email is required"}), 400
            
        # In a real app, you would save the email to a database (like SQLite or PostgreSQL) 
        # or send it to an email marketing service (like Mailchimp).
        print(f"New subscriber added to list: {email}")
        
        return jsonify({
            "status": "success",
            "message": "Thanks for subscribing!"
        }), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the server
if __name__ == '__main__':
    # debug=True automatically restarts the server when you make code changes
    print("Starting TrendDrop server on http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
