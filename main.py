# Autor: Helder Henrique da Silva
# Data: 04/06/2023
# Descrição: Simulador de Relógio Vetorial para a disciplina de Sistemas Distribuídos
# Professor: Jim Lau
#

import tkinter as tk
from tkinter import ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class Processo:
    """
    Classe que representa um processo em um sistema distribuído.

    Atributos:
        - id (int): O identificador do processo.
        - relogio (list): Lista que representa o vetor de relógio do processo.
        - historico_eventos (list): Lista que guarda o histórico de eventos do processo.
        - historico_mensagens (list): Lista que guarda o histórico de mensagens enviadas pelo processo.

    Métodos:
        - evento_local(): Realiza um evento local no processo, incrementando o relógio e registrando o evento.
        - enviar_mensagem(outro_processo): Envia uma mensagem para outro processo, incrementando o relógio e registrando o evento.
        - receber_mensagem(relogio_externo): Recebe uma mensagem de outro processo, atualiza o relógio e registra o evento.
    """

    def __init__(self, id, n_processos):
        """
        Inicializa uma instância da classe Processo.

        Parâmetros:
            - id (int): O identificador do processo.
            - n_processos (int): O número total de processos no sistema distribuído.
        """
        self.id = id
        self.relogio = [0] * n_processos
        self.historico_eventos = []
        self.historico_mensagens = []

    def evento_local(self):
        """
        Realiza um evento local no processo, incrementando o relógio e registrando o evento.
        """
        self.relogio[self.id] += 1
        self.historico_eventos.append(list(self.relogio))
        self.historico_mensagens.append(None)

    def enviar_mensagem(self, outro_processo):
        """
        Envia uma mensagem para outro processo, incrementando o relógio e registrando o evento.

        Parâmetros:
            - outro_processo (Processo): O processo destino da mensagem.
        """
        self.relogio[self.id] += 1
        self.historico_eventos.append(list(self.relogio))
        posicao_evento_destino = outro_processo.receber_mensagem(self.relogio)
        self.historico_mensagens.append(
            (outro_processo.id, posicao_evento_destino))

    def receber_mensagem(self, relogio_externo):
        """
        Recebe uma mensagem de outro processo, atualiza o relógio e registra o evento.

        Parâmetros:
            - relogio_externo (list): O vetor de relógio recebido na mensagem.

        Retorna:
            - posicao_evento_destino (int): A posição do evento no histórico de eventos do processo.
        """
        self.relogio = [max(a, b)
                        for a, b in zip(self.relogio, relogio_externo)]
        self.relogio[self.id] += 1
        self.historico_eventos.append(list(self.relogio))
        self.historico_mensagens.append(None)
        return len(self.historico_eventos) - 1


class App:
    """
    Classe que representa a aplicação GUI do simulador de vetor de relógio.

    Atributos:
        - root (Tk): A janela principal da aplicação.
        - processos (list): Lista que guarda os processos do sistema distribuído.
        - labels (list): Lista que guarda as labels de exibição dos relógios dos processos.
        - fig (Figure): A figura do gráfico de relógios.
        - canvas (FigureCanvasTkAgg): O objeto de exibição do gráfico de relógios.

    Métodos:
        - __init__(root): Inicializa uma instância da classe App.
        - criar_simulacao(): Cria a simulação do vetor de relógio com base no número de processos selecionado.
        - encerrar_simulacao(): Encerra a simulação do vetor de relógio.
        - evento_local(id_processo): Realiza um evento local em um processo.
        - enviar_mensagem(id_origem, id_destino): Envia uma mensagem de um processo para outro.
        - atualizar_labels(): Atualiza as labels de exibição dos relógios dos processos.
        - atualizar_grafico(): Atualiza o gráfico de relógios.
    """

    def __init__(self, root):
        """
        Inicializa uma instância da classe App.

        Parâmetros:
            - root (Tk): A janela principal da aplicação.
        """
        self.root = root
        self.processos = []
        self.labels = []
        self.fig = Figure(figsize=(10, 5))
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.create_frame = tk.Frame(self.root, background='white')
        self.create_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.title_label = tk.Label(self.create_frame, text='Simulador de Vetor de Relógio', font=(
            "Helvetica", 16), background='white')
        self.title_label.pack(pady=10)

        self.processos_var = tk.StringVar()
        self.processos_combobox = ttk.Combobox(
            self.create_frame, textvariable=self.processos_var,
            values=[str(i) for i in range(1, 6)], state='readonly')
        self.processos_combobox.set('1')  # Definir o valor inicial como 1
        self.processos_combobox.pack(pady=10)

        self.create_button = tk.Button(
            self.create_frame, text="Criar simulação de relógio vetorial", command=self.criar_simulacao, background='lightblue', padx=10, pady=10)
        self.create_button.pack()

    def criar_simulacao(self):
        """
        Cria a simulação do vetor de relógio com base no número de processos selecionado.
        """
        num_processos = int(self.processos_var.get())
        self.processos = [Processo(i, num_processos)
                          for i in range(num_processos)]
        self.create_frame.pack_forget()

        # Criar um canvas e adicionar uma barra de rolagem
        self.canvas_frame = tk.Canvas(self.root, background='white')
        self.canvas_frame.config(width=10)
        self.scrollbar = tk.Scrollbar(
            self.root, command=self.canvas_frame.yview)
        self.canvas_frame.configure(yscrollcommand=self.scrollbar.set)
        self.canvas_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.LEFT, fill=tk.Y)

        # Criar um frame para adicionar os botões e labels
        self.sim_frame = tk.Frame(self.canvas_frame, background='white')
        self.canvas_frame.create_window(
            (0, 0), window=self.sim_frame, anchor='nw')

        # Configurar a scrollregion do Canvas após o Frame ser preenchido com botões e labels
        self.sim_frame.bind('<Configure>', lambda e: self.canvas_frame.configure(
            scrollregion=self.canvas_frame.bbox('all')))
        self.canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)
        self.end_button = tk.Button(
            self.sim_frame, text="Encerrar simulação", command=self.encerrar_simulacao, background='lightblue', padx=10, pady=10)
        self.end_button.pack(pady=10, anchor='n', side=tk.TOP)
        self.atualizar_labels()

    def encerrar_simulacao(self):
        """
        Encerra a simulação do vetor de relógio.
        """
        for label in self.labels:
            label.destroy()
        self.labels = []
        self.processos = []
        self.end_button.destroy()
        self.fig.clear()
        self.canvas.get_tk_widget().pack_forget()

        # Destruir a barra de rolagem
        self.scrollbar.destroy()
        # Limpar o Canvas
        self.canvas_frame.delete("all")
        self.canvas_frame.pack_forget()
        self.sim_frame.destroy()  # Destruir o frame da simulação

        # Reorganizar o frame de criação
        self.create_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def evento_local(self, id_processo):
        """
        Realiza um evento local em um processo.

        Parâmetros:
            - id_processo (int): O ID do processo.
        """
        self.processos[id_processo].evento_local()
        self.atualizar_labels()

    def enviar_mensagem(self, id_origem, id_destino):
        """
        Envia uma mensagem de um processo para outro.

        Parâmetros:
            - id_origem (int): O ID do processo de origem.
            - id_destino (int): O ID do processo de destino.
        """
        self.processos[id_origem].enviar_mensagem(self.processos[id_destino])
        self.atualizar_labels()

    def atualizar_labels(self):
        """
        Atualiza as labels de exibição dos relógios dos processos.
        """
        for label in self.labels:
            label.destroy()
        self.labels = []
        for i, processo in enumerate(self.processos):
            label = tk.Label(
                self.sim_frame, text=f"Processo {i}: {processo.relogio}", background='white')
            label.pack(pady=5)
            self.labels.append(label)
            local_event_button = tk.Button(
                self.sim_frame, text=f"Evento Local Processo {i}", command=lambda i=i: self.evento_local(i), background='lightblue')
            local_event_button.pack(pady=5)
            self.labels.append(local_event_button)
            for j in range(len(self.processos)):
                if i != j:
                    send_message_button = tk.Button(
                        self.sim_frame, text=f"Processo {i} -> Processo {j}", command=lambda i=i, j=j: self.enviar_mensagem(i, j), background='lightblue')
                    send_message_button.pack(pady=5)
                    self.labels.append(send_message_button)
        self.atualizar_grafico()

    def atualizar_grafico(self):
        """
        Atualiza o gráfico de relógios.
        """
        self.fig.clear()
        ax = self.fig.add_subplot(111)
        for i, processo in enumerate(self.processos):
            y = [i] * len(processo.historico_eventos)
            x = list(range(len(processo.historico_eventos)))
            ax.plot(x, y, marker='o')
            for j, clock in enumerate(processo.historico_eventos):
                marker_x = j
                marker_y = i
                text_x = marker_x - 0.005  # Deslocamento horizontal para centralizar
                text_y = marker_y + 0.005  # Deslocamento vertical para ficar acima
                # Ajuste: posicionar o texto do vetor
                ax.text(text_x, text_y, str(clock), ha='center', va='bottom')
                if processo.historico_mensagens[j] is not None:
                    id_destino, posicao_evento_destino = processo.historico_mensagens[j]
                    ax.annotate("", xy=(posicao_evento_destino, id_destino), xytext=(
                        marker_x, marker_y), arrowprops=dict(arrowstyle="->"))
        # Definir os valores dos ticks no eixo Y
        ax.set_yticks(list(range(len(self.processos))))
        # Definir rótulos personalizados para os ticks no eixo Y
        ax.set_yticklabels(
            [f"P {i}" for i in range(len(self.processos))])
        # Remover o comprimento dos ticks no eixo Y
        ax.tick_params(axis='y', which='both', length=0)
        ax.xaxis.set_visible(False)  # Remover o eixo X do gráfico
        self.canvas.draw()


root = tk.Tk()
root.geometry('1400x800')
root.title("Simulador de Vetor de Relógio")
app = App(root)
root.mainloop()
