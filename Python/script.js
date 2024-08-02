const letterFrequency =(phrase) =>{

         let frequency={}
         for(const letter of phrase){
             if(letter in frequency){
                 frequency[letter] += 1
             }
          else{
                 frequency[letter] = 1
             }
         }
         return frequency
     }