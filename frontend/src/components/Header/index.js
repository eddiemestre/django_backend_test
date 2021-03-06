import React from "react";
import { HeadContainer, AppHead } from './Styles.js';
import { useNavigate } from "react-router-dom";

const Header = () => {
    const navigate = useNavigate();

    const handleOnClick = async () => {
        navigate("/login")
    }

    return (
        <HeadContainer>
            <AppHead onClick={() => handleOnClick()}>The Food App</AppHead>
        </HeadContainer>
    );
};

export default Header;