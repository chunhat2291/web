import streamlit as st
import time

st.title("Form đăng ký tài khoản")

# Nhập thông tin
tai_khoan = st.text_input("Tài khoản")
mat_khau = st.text_input("Mật khẩu", type="password")
nhap_lai = st.text_input("Nhập lại mật khẩu", type="password")
ten_nguoi_dung = st.text_input("Tên người dùng")
email = st.text_input("Email")

# Tính xem đã điền bao nhiêu%
so_truong_da_dien = 0

if tai_khoan:
    so_truong_da_dien += 1
if mat_khau:
    so_truong_da_dien += 1
if nhap_lai:
    so_truong_da_dien += 1
if ten_nguoi_dung:
    so_truong_da_dien += 1
if email:
    so_truong_da_dien += 1

tong_truong = 5
phan_tram = int((so_truong_da_dien / tong_truong) * 100)

# Thanh tiến độ
st.progress(phan_tram)
st.write("Bạn đã hoàn thành:", phan_tram, "%")

# Nút đăng ký
if st.button("Đăng ký"):
    if so_truong_da_dien < 5:
        st.error("Bạn chưa điền đủ thông tin!")
    elif mat_khau != nhap_lai:
        st.error("Mật khẩu không trùng nhau!")
    else:
        st.success("Đăng ký thành công!")
        st.balloons()
