import React from 'react';

export const Great = (props) => {  // ES6
  var {product} = props
  return(
      <>
          <div className='Widget__Basis'>
            {product.id}----{product.name}
            <LikeBtn tweet={product}/>  <DislikeBtn tweet={product}/>
          </div>
          <br />
      </>
  )
}

function LikeBtn(props){
  const {tweet} = props
  return(
    <button action={{type: "like"}}> {tweet.get_nb_likes} Like </button>
  )
}

function DislikeBtn(props){
  const {tweet} = props
  return(
    <button action={{type: "dislike"}} > {tweet.get_nb_unlikes} Unlike </button>
  )
}
