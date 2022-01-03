import React from 'react';
import './mypage.css';

fetch("http://localhost:8081/mypage").then((response) =>
        console.log(response));
        
const Template = ({form, children}) => {
  return (
    <main className="template">
      <div className="title">
        백앤드 내용
        
      </div>
    </main>
  );
};

export default Template;