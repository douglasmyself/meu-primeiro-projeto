# Sistema de Gestão Escolar - Projetado por Douglas Gomes de Almeida
# Licenciatura em Computação - Estácio

class GerenciadorTurma:
    def __init__(self, nome_turma):
        self.nome_turma = nome_turma
        self.alunos = []

    def adicionar_aluno(self, nome, nota1, nota2):
        media = (nota1 + nota2) / 2
        status = "Aprovado" if media >= 7.0 else "Recuperação / Reprovado"
        
        aluno = {
            "nome": nome,
            "nota1": nota1,
            "nota2": nota2,
            "media": media,
            "status": status
        }
        self.alunos.append(aluno)
        print(f"\n✅ Aluno {nome} cadastrado com sucesso!")

    def listar_alunos(self):
        if not self.alunos:
            print("\n⚠️ Nenhum aluno cadastrado até o momento.")
            return

        print(f"\n--- Relatório da Turma: {self.nome_turma} ---")
        for i, aluno in enumerate(self.alunos, 1):
            print(f"{i}. Nome: {aluno['nome']} | Média: {aluno['media']:.1f} | Status: {aluno['status']}")

    def calcular_media_turma(self):
        if not self.alunos:
            return 0.0
        total_notas = sum(aluno["media"] for aluno in self.alunos)
        return total_notas / len(self.alunos)

def menu():
    turma = GerenciadorTurma("Pensamento Computacional - 2026")
    
    while True:
        print("\n==============================")
        print("  SISTEMA DE GESTÃO ESCOLAR   ")
        print("==============================")
        print("1. Cadastrar Aluno e Notas")
        print("2. Listar Todos os Alunos")
        print("3. Ver Média Geral da Turma")
        print("4. Sair")
        
        opcao = input("Escolha uma opção (1-4): ")

        if opcao == "1":
            nome = input("Nome do aluno: ")
            try:
                n1 = float(input("Primeira Nota: "))
                n2 = float(input("Segunda Nota: "))
                turma.adicionar_aluno(nome, n1, n2)
            except ValueError:
                print("\n❌ Erro: Por favor, insira valores numéricos válidos para as notas.")
        
        elif opcao == "2":
            turma.listar_alunos()
            
        elif opcao == "3":
            media = turma.calcular_media_turma()
            print(f"\n📊 Média Geral da Turma: {media:.2f}")
            
        elif opcao == "4":
            print("\nEncerrando o sistema. Até logo!")
            break
        else:
            print("\n❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
