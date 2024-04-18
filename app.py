from flask import Flask, render_template

app = Flask(__name__)

@app.route('/profile')#define route
def profile():#Define pages
    return render_template('profile.html')

@app.route('/profile/edit')#define route
def profile_edit():#Define pages
    return render_template('update_my_profile.html')

@app.route('/profile/blog')
def blog():
    return render_template('blog_detail_page.html')

if __name__ == '__main__':
    app.run(debug=True)