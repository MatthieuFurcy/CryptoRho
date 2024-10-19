# Programmation autour des nombres premiers - Décomposition en facteurs premiers

## Auteur
M. Matthieu Furcy

## Date
2024-10-19

## Description
Ce projet implémente une méthode de décomposition en facteurs premiers d'entiers en utilisant l'algorithme de Pollard's Rho. Ce dernier est réputé pour sa rapidité dans la factorisation des entiers, en particulier pour les nombres semi-premiers. L'algorithme inclut une gestion optimisée pour les petits facteurs afin d'éviter les échecs sur de petits nombres.

## Méthodologie
1. **Définition de la méthode `int_factor`** utilisant l'algorithme de Pollard's Rho.
2. **Gestion des cas triviaux**, y compris le traitement des nombres pairs.
3. **Vérification des petits facteurs** jusqu'à 1000 pour une optimisation immédiate.
4. **Calcul du GCD** avec l'algorithme d'Euclide.
5. **Fonction polynomiale** pour générer une séquence d'entiers, permettant de détecter les cycles et trouver les facteurs.
6. **Retour des facteurs** sous forme de dictionnaire avec leurs exposants respectifs.
7. **Inclusion d'exemples d'utilisation** et d'assertions pour valider la fonctionnalité.

## Installation
Clonez le dépôt et exécutez le script avec Python 3.x.

```bash
git clone https://github.com/ZitiixDevelopment/nom_du_depot.git
cd nom_du_depot
python3 votre_script.py
