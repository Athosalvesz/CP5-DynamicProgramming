import sys

INF = float('inf')

def qtdeMoedas(M, moedas):


    moedas_ordenadas = sorted(moedas, reverse=True)
    
    qtde = 0
    m_restante = M
    
    for c in moedas_ordenadas:
        if m_restante >= c:
            num_moedas_c = m_restante // c
            qtde += num_moedas_c
            m_restante -= (num_moedas_c * c)
        
    return qtde


def _qtdeMoedasRec_helper(M, moedas)
  
    if M == 0:
        return 0

    if M < 0:
        return INF

    min_necessario = INF
    

    for c in moedas:
      
        res = _qtdeMoedasRec_helper(M - c, moedas)
        
      
        if res != INF:
            min_necessario = min(min_necessario, 1 + res)
            
    return min_necessario

def qtdeMoedasRec(M, moedas):

    resultado = _qtdeMoedasRec_helper(M, moedas)
    
 
    return -1 if resultado == INF else int(resultado)

def _qtdeMoedasRecMemo_helper(M, moedas, memo):

    if M == 0:
        return 0
    if M < 0:
        return INF
    

    if M in memo:
        return memo[M]
    
    min_necessario = INF
    
    for c in moedas:
        res = _qtdeMoedasRecMemo_helper(M - c, moedas, memo)
        
        if res != INF:
            min_necessario = min(min_necessario, 1 + res)
            

    memo[M] = min_necessario
    return min_necessario

def qtdeMoedasRecMemo(M, moedas):

    memo = {} 
    resultado = _qtdeMoedasRecMemo_helper(M, moedas, memo)
    
    return -1 if resultado == INF else int(resultado)


def qtdeMoedasPD(M, moedas):

 
    dp = [INF] * (M + 1)
    
  
    dp[0] = 0
    

    for i in range(1, M + 1):
       
        for c in moedas:
             
            if c <= i:
            
                dp[i] = min(dp[i], 1 + dp[i - c])
                

    return -1 if dp[M] == INF else int(dp[M])


if __name__ == "__main__":
    
    print("--- Teste com M=6, moedas=[1, 3, 4] ---")
    M_teste = 6
    moedas_teste = [1, 3, 4]

    
    print(f"Gulosa: {qtdeMoedas(M_teste, moedas_teste)}")

 
    print(f"Recursiva Pura: {qtdeMoedasRec(M_teste, moedas_teste)}")


    print(f"Memoization (Top-Down): {qtdeMoedasRecMemo(M_teste, moedas_teste)}")

 
    print(f"PD (Bottom-Up): {qtdeMoedasPD(M_teste, moedas_teste)}")

    print("\n--- Teste de impossibilidade M=7, moedas=[2, 4] ---")
    M_teste_2 = 7
    moedas_teste_2 = [2, 4]
    
   
    print(f"Recursiva Pura: {qtdeMoedasRec(M_teste_2, moedas_teste_2)}")
    print(f"Memoization (Top-Down): {qtdeMoedasRecMemo(M_teste_2, moedas_teste_2)}")

    print(f"PD (Bottom-Up): {qtdeMoedasPD(M_teste_2, moedas_teste_2)}")
