{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Calculadora",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyMKNVaM3uJzvxA/L1CD3/37",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/marimartignago/marimartignago.github.io/blob/master/Calculadora.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "bi-XIFkYEBNl"
      },
      "source": [
        ""
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "msb9Azh4Q5AB"
      },
      "source": [
        "# Autora: Mariana Martignago.\n",
        "# Feito para o desafio técnico ProWay - parte 1.\n",
        "\n",
        "\n",
        "valor_em_reais = float(input(\"Valor a ser investido em anúncios: \"))\n",
        "\n",
        "def calculadora_anuncios(valor_em_reais):\n",
        "  if valor_em_reais < 0.01:\n",
        "    print(\"Erro: Valor inválido. O valor deve ser maior do que 1 centavo.\")\n",
        "\n",
        "  else:\n",
        "    # Para cada 1 real investido, 30 anúncios originais serão visualizados. .\n",
        "    alcance_anuncio_original = valor_em_reais * 30\n",
        "\n",
        "    # A cada 100 pessoas que visualizam o anúncio 12 clicam nele.\n",
        "    clicam = alcance_anuncio_original / 100 * 12\n",
        "\n",
        "    # A cada 20 pessoas que clicam no anúncio 3 compartilham nas redes sociais.\n",
        "    compartilham = clicam / 20 * 3\n",
        "\n",
        "    # Cada compartilhamento nas redes sociais gera 40 novas visualizações.\n",
        "    # O mesmo anúncio é compartilhado no máximo 4 vezes em sequência. \n",
        "    novas_visualizacoes = (compartilham * 4) * 40\n",
        "\n",
        "    # Cálculo do máximo de visualizações possível.\n",
        "    valor_final = round(alcance_anuncio_original + novas_visualizacoes)\n",
        "\n",
        "    return f\"Projeção aproximada da quantidade máxima de pessoas que visualizarão o mesmo anúncio (considerando o anúncio original + os compartilhamentos): {valor_final}\"\n",
        "\n",
        "# Função sendo chamada\n",
        "calculadora_anuncios(valor_em_reais)"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}