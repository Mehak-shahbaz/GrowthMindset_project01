#streamlit
import streamlit as st # type: ignore

st.set_page_config(page_title = "growth mindset project", page_icon ="⭐")
st.title("Growth Mindset Challenge:Web App with Streamlit ")

st.header("🚀Welcome to your Growth Journey!")
st.write("Embrace challenge, learn from mistakes, and unlock your full potential.This Al-powered app helps you build a growth mindset with reflection,challenges, and achevements!☀️")

#quote section
st.header("💡Today's Growth Mindset Quote")
st.write("Success is not final,failure is not fatal: it is courage to continue that counts. -winston churchill")

st.header("🔧What's your challenge Today?")
user_input = st.text_input("Describe a challenge you are facing:")

#condition
if user_input:
    st.success(f"💪you are facing:{user_input}. Keep pushing towards your goal!🚀")
else:
    st.warning("Tell us about your challenge to get started!")

#reflexing
st.header(" Reflect on your Learning")
reflection = st.text_area("write your reflections here:")

if reflection:
    st.success(f"✨Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflecting on past experience help you grow! Share your difficulties")


#achievements
st.header("🏆Celebrate Your Wins!")
achievement = st. text_input("Share somthing you are recently accomplished:")

if achievement:
    st.success(f"🎇Amazing! you achieved: {achievement}")
else:
    st.info("Big or small , every achievement counts! Share one now!")

#footer
st.write("- - -")
st.write("🚀 Keep believing in yourself.Growth is a journey, not a destination!🌟")
st.write("⛔**Created by Mehak shahbaz**")
