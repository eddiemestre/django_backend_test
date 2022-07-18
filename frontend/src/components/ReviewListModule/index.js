import React, {useEffect, useState} from "react";
import { ReviewModule, ReviewTitle, ReviewDate, ReviewPreview } from './Styles.js';
import { useNavigate, useParams } from "react-router-dom";
import { formatDate } from "../../utils/FormatDate.js";

const ReviewListModule = ({ review }) => {
    const [formattedDate, setformattedDate] = useState(review.date || null)
    const [rerender, setRerender] = useState(false);
    const navigate = useNavigate();
    const params = useParams();


    useEffect(() => {
        if (formattedDate) {
            setformattedDate(formatDate(formattedDate))
        } else {
            setformattedDate(null)
        }
        setRerender(!rerender)  // dummy state
    }, [])


    const handleClick = (event) => {
        console.log(event)
        navigate(`/user/${params.username}/${event}`)
    }

    return(
        <ReviewModule onClick={() => handleClick(review.id)}>
            <ReviewTitle>
                {review.title}
            </ReviewTitle>
            <ReviewDate>
                {formattedDate}
            </ReviewDate>
            <ReviewPreview>
                {review.review}
            </ReviewPreview>
        </ReviewModule>
        
    );
}

export default ReviewListModule;