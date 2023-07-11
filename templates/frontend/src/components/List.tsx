// import React from 'react';
import type { PropsWithChildren } from 'react';

type GreatProps = PropsWithChildren<{
  product: {
    id?: number,
    name?: string
  }
}>

export const Great = (props: GreatProps) => {  // ES6
  // POURQUOI REACT INTERPRETE LES COMPONENTS EN 2 FOIS ?
  return(
      <>
          <div className='Widget__Basis'>
            {props.product.id}----{props.product.name}
          </div>
          <br/>
      </>
  )
}

/************************************ Faire un Composant en .tsx **************************************/
// import type { FunctionComponent, PropsWithChildren } from 'react';
// import React, { Children } from 'react';


// type Props = PropsWithChildren<{
//   start?: number;
// }>

// export const Counter: FunctionComponent<Props> = ({start=0, children}) => {
//   const [n , setN] = useState<number>{start}
//   const ref = useRef<HTMLButtonElement>{null}
//   const incr = () => setN(n=>n++j)
//   return <>
//     <h2> Compteur </h2>
//       {Children}
//     <p>
//       Numéro: {start}
//     </p>
//     <button ref={ref} onclick={incr}>
//       Incrementer
//     </button>
//   </>
// }